from django.urls import path
from .views import signup_view, profile, login_view, logout_view


urlpatterns = [
    path('login/', login_view, name='login'),
    path('signup/', signup_view, name='signup'),
    path('logout/', logout_view, name='logout'),
]
# path('signup/', signup, name='signup'),
#     path('profile/', profile, name='profile'),
#     path('login/', login_view, name='login'),