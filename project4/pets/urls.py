from django.urls import path
from .views import get_info, get_pets, detail



urlpatterns = [
    path('', get_info, name='get_info'),
    path('pets/<int:pk>', get_pets, name='get_pets'),
    path('pets/detail/<int:pk>', detail, name='detail')
]