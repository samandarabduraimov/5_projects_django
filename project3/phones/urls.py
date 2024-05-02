from django.urls import path
from .views import get_info, get_phones, detail



urlpatterns = [
    path('', get_info, name='get_info'),
    path('phones/<int:pk>', get_phones, name='get_phones'),
    path('phones/detail/<int:pk>', detail, name='detail')
]