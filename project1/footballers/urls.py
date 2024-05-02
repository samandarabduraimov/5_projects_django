from django.urls import path
from .views import get_info, get_footballers, detail



urlpatterns = [
    path('', get_info, name='get_info'),
    path('footballers/<int:pk>', get_footballers, name='get_footballers'),
    path('footballers/detail/<int:pk>', detail, name='detail')
]