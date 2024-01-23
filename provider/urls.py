from django.urls import path

from provider.views import ProviderList, ProviderDetail, ProviderCreate, ProviderUpdate, ProviderDelete
from provider.apps import RetailConfig

app_name = RetailConfig.name

urlpatterns = [
    path('', ProviderList.as_view(), name='provider-list'),
    path('create/', ProviderCreate.as_view(), name='provider-create'),
    path('<int:pk>/', ProviderDetail.as_view(), name='provider-detail'),
    path('update/<int:pk>/', ProviderUpdate.as_view(), name='provider-update'),
    path('delete/<int:pk>/', ProviderDelete.as_view(), name='provider-delete'),
]
