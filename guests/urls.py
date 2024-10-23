from django.urls import path
from . import views

urlpatterns = [
    path('', views.guest_list, name='guest_list'),  # Add views. before guest_list
    path('create/', views.guest_create, name='guest_create'),  # Add views. before guest_create
    path('<int:pk>/', views.guest_detail, name='guest_detail'),  # Add views. before guest_detail
    path('<int:pk>/update/', views.guest_update, name='guest_update'),  # Add views. before guest_update
    path('delete/<int:pk>/', views.guest_delete, name='guest_delete'),  # This line is already correct
]
