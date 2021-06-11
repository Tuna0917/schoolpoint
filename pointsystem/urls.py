from django.urls import path
from .views import *

urlpatterns = [
    path('home/', home, name='home'),
    path('croom/',create_room,name='c_room'),
    path('room/', RoomListView.as_view(), name='room_list'),
    path('room/<int:pk>/', RoomDetailView.as_view(), name='room_detail'),
]
