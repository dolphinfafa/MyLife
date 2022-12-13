from django.urls import path
from .views import index, test, ajax_login

urlpatterns = [
    path('', index),
    path('test/', test),
    path('ajax_login_data/', ajax_login)
]