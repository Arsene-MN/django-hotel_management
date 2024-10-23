from django.urls import path
from . import views

urlpatterns = [
    path('', views.booking_list, name='booking_list'),
    path('create/', views.create_booking, name='create_booking'),
    path('<int:pk>/', views.booking_detail, name='booking_detail'),
    path('<int:pk>/update/', views.booking_update, name='booking_update'),
    path('delete/<int:pk>/', views.booking_delete, name='booking_delete'),
]
