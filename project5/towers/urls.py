from django.urls import path
from .views import get_info, get_towers, detail



urlpatterns = [
    path('', get_info, name='get_info'),
    path('towers/<int:pk>', get_towers, name='get_towers'),
    path('towers/detail/<int:pk>', detail, name='detail')
]