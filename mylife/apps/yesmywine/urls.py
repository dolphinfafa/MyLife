from django.urls import path
from .views import InventView

urlpatterns = [
    path('invent', InventView.as_view(), name='YesMyWine Ivent')
]