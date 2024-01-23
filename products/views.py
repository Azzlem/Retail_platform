from drf_yasg.utils import swagger_auto_schema
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from products.models import Product
from products.serializers import ProductSerializer
from users.models import User
from users.permissions import IsOwnerOrStaffProduct


class ProductViewSet(ModelViewSet):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()

    def get_permissions(self):
        """
        Instantiates and returns the list of permissions that this view requires.
        """
        if self.action in ['list', 'create']:
            permission_classes = [IsAuthenticated]
        else:
            permission_classes = [IsOwnerOrStaffProduct, IsAuthenticated]
        return [permission() for permission in permission_classes]

    def perform_create(self, serializer):
        """
        Создание продукта и установление владельца.
        """
        product = serializer.save()
        product.owner = get_object_or_404(User, id=self.request.user.id)
        product.save()
