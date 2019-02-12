from django.urls import path
from .views import SaleApiView
urlpatterns = [
    path('type_sale/<str:type>/<str:material>/', SaleApiView.as_view())
]