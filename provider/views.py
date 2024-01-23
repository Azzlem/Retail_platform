from drf_yasg.utils import swagger_auto_schema
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from provider.models import Provider
from provider.serializers import RetailSerializerView, ProviderSerializer, ProviderSerializerUpdate
from users.permissions import IsOwnerOrStaffProductProvider


class ProviderList(generics.ListAPIView):
    queryset = Provider.objects.all()
    serializer_class = RetailSerializerView
    permission_classes = [IsAuthenticated, ]

    @swagger_auto_schema(operation_summary="Список поставщиков")
    def get(self, request, *args, **kwargs):
        return super(ProviderList, self).get(request, *args, **kwargs)


class ProviderDetail(generics.RetrieveAPIView):
    queryset = Provider.objects.all()
    serializer_class = RetailSerializerView
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(operation_summary="Поставщик")
    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)


class ProviderCreate(generics.CreateAPIView):
    serializer_class = ProviderSerializer
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(operation_summary="Создать поставщика")
    def post(self, request, *args, **kwargs):
        return super(ProviderCreate, self).post(request, *args, **kwargs)

    def perform_create(self, serializer):
        new_provider = serializer.save()
        new_provider.author = self.request.user
        new_provider.save()


class ProviderUpdate(generics.UpdateAPIView):
    serializer_class = ProviderSerializerUpdate
    queryset = Provider.objects.all()
    permission_classes = [IsOwnerOrStaffProductProvider, IsAuthenticated]

    @swagger_auto_schema(operation_summary="Изменить информацию о поставщике")
    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    @swagger_auto_schema(operation_summary="Изменить информацию о поставщике")
    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)


class ProviderDelete(generics.DestroyAPIView):
    queryset = Provider.objects.all()
    permission_classes = [IsOwnerOrStaffProductProvider, IsAuthenticated]
    serializer_class = ProviderSerializer

    @swagger_auto_schema(operation_summary="Удаление поставщика")
    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
