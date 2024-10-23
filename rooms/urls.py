from django.urls import path
from .views import room_list, room_detail, room_create, room_update, room_delete
from . import views

app_name = 'rooms'

urlpatterns = [
    path('', views.room_list, name='room_list'),
    path('create/', views.room_create, name='room_create'),   
    path('<int:pk>/', views.room_detail, name='room_detail'),
    path('<int:pk>/update/', views.room_update, name='room_update'),
    path('<int:pk>/delete/', views.room_delete, name='room_delete'),
]
