from django.contrib import admin
from django.urls import path, include
from rooms import views
from users.views import login_view 

urlpatterns = [
    path('', login_view, name='login'),
    path('admin/', admin.site.urls),
    path('guests/', include('guests.urls')),
    path('rooms/', include('rooms.urls')),
    path('bookings/', include('bookings.urls')),
    path('users/', include('users.urls')),
]
    