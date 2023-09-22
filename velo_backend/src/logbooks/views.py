from django.core.exceptions import ObjectDoesNotExist
from django.http import Http404
from rest_framework import permissions
from rest_framework import viewsets, generics
from rest_framework import filters
from rest_framework.parsers import MultiPartParser, FormParser

from src.bicycles.models import Bicycle
from src.logbooks.models import LogBookRecord, LogBookRecordPictures
from src.logbooks.permissions import IsBicycleOwner, IsRecordCreator
from src.logbooks.serializers import LogBookRecordSerializer, LogBookRecordPictureSerializer


class LogBookRecordViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = LogBookRecordSerializer
    filter_backends = [filters.OrderingFilter]
    ordering_fields = ['id']

    def get_queryset(self):
        amount_first = self.request.query_params.get('first')
        amount_last = self.request.query_params.get('last')
        amount_random = self.request.query_params.get('random')

        if amount_first:
            queryset = LogBookRecord.objects.order_by('id')[:int(amount_first)]
        elif amount_last:
            queryset = LogBookRecord.objects.order_by('-id')[:int(amount_last)]
        elif amount_random:
            queryset = LogBookRecord.objects.order_by('?')[:int(amount_random)]
        else:
            queryset = LogBookRecord.objects.all()
        # TODO: добавить условие, чтобы возвращались только активные (не бывшие) велосипеды
        return queryset


class BicycleLogBookViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = LogBookRecordSerializer

    def get_queryset(self):
        bicycle_pk = self.kwargs.get('pk')
        queryset = LogBookRecord.objects.filter(bicycle=bicycle_pk).order_by('-id')
        return queryset


class BicycleLogBookRecordCreateView(generics.CreateAPIView):
    permission_classes = [IsBicycleOwner]
    serializer_class = LogBookRecordSerializer
    parser_classes = (MultiPartParser, FormParser,)

    # TODO: !! добавить обработку(сжатие) фото перед сохранением, возможно потребуется сохранение 
    # в двух разных разрешениях (большое и маленькое), для отображения в разных местах
    def perform_create(self, serializer):
        bicycle_pk = self.kwargs.get('pk')  # - можно брать просто из словаря (self.kwargs['pk']), но если не будет pk, то вернется исключени, а если брать через get то вернется не исключение а просто None
        bicycle = Bicycle.objects.get(pk=bicycle_pk)
        print(f"Received files: {self.request.FILES}")
        print(f"Received data: {self.request.data}")
        obj = serializer.save(bicycle=bicycle, creator=self.request.user)

        # TODO: разобраться, почему не отправляется с именем pictures (возникает ошибка о том, что ожиадается
        #  словарь), но отпарвялсяется с любым другим именем (сейчас чтоб обойти ошибку отправлею с picturess)
        pictures = self.request.FILES
        print('pictures---', pictures)

        for key, img in pictures.items():
            # print('k', key)
            # print('v', img)
            LogBookRecordPictures.objects.create(image=img, pictures=obj)
        # TODO: скорее всего возврат obj не нужен
        return obj


class LogBookRecordUpdateView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsRecordCreator]
    serializer_class = LogBookRecordSerializer

    def get_object(self):
        print(f"Received data: {self.request.data}")
        record_pk = self.kwargs.get('pk')
        self.obj = LogBookRecord.objects.get(pk=record_pk)
        return self.obj

    def perform_update(self, serializer):
        pictures = self.request.FILES

        for key, img in pictures.items():
            LogBookRecordPictures.objects.create(image=img, pictures=self.obj)
        serializer.save()


class LogBookRecordPictureDeleteView(generics.DestroyAPIView):
    # TODO: !! настроить, чтоб фото мог удалять только создатель
    # permission_classes = [IsRecordCreator]
    serializer_class = LogBookRecordPictureSerializer

    # def get_queryset(self):
    #     picture_id = self.kwargs.get('picture_id')
    #     return LogBookRecordPictures.objects.get(id=picture_id)
    def get_object(self):
        picture_pk = self.kwargs.get('picture_pk')
        try:
            return LogBookRecordPictures.objects.get(pk=picture_pk)
        except ObjectDoesNotExist:
            raise Http404

