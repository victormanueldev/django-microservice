from django.urls import path
from .views import SaleApiView
from .views import SalePostApiView
urlpatterns = [
    path('type_sale/<str:type_sale>/<str:material>/', SaleApiView.as_view()),
    path('type_sale/', SalePostApiView.as_view())
]