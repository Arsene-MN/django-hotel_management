from django.urls import path
from .views import room_list, room_detail, room_create, room_update, room_delete

app_name = 'rooms'

urlpatterns = [
    path('', room_list, name='room_list'),
    path('create/', room_create, name='room_create'),   
    path('<int:pk>/', room_detail, name='room_detail'),
    path('<int:pk>/update/', room_update, name='room_update'),
    path('<int:pk>/delete/', room_delete, name='room_delete'),
]
