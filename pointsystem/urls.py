from django.urls import path
from .views import *

urlpatterns = [
    path('home/', home, name='home'),
    path('', home, name='hello'),
    path('croom/',create_room,name='c_room'),
    path('room/', RoomListView.as_view(), name='room_list'),
    path('room/<int:pk>/', RoomDetailView.as_view(), name='room_detail'),
    path('room/<int:pk>/delete/', RoomDeleteView.as_view(), name='d_room'),
    path('student/signup/', student_signup, name='student_signup')
]
