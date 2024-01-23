from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from products.models import Product
from products.serializers import ProductSerializer
from users.permissions import IsOwnerOrStaff


class ProductView(viewsets.ViewSet):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()

    def list(self, request):
        pass

    def create(self, request):
        pass

    def retrieve(self, request, pk=None):
        pass

    def update(self, request, pk=None):
        pass

    def partial_update(self, request, pk=None):
        pass

    def destroy(self, request, pk=None):
        pass

    def get_permissions(self):
        """
        Instantiates and returns the list of permissions that this view requires.
        """
        if self.action == 'list':
            permission_classes = [IsAuthenticated]
        else:
            permission_classes = [IsOwnerOrStaff]
        return [permission() for permission in permission_classes]
