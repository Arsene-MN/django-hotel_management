from django.urls import path
from django.contrib.auth.views import LogoutView  
from .views import signup_view, profile, login_view


urlpatterns = [
    path('login/', login_view, name='login'),
    path('signup/', signup_view, name='signup'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    path('logout/', LogoutView.as_view(next_page='home'), name='logout'),
]
# path('signup/', signup, name='signup'),
#     path('profile/', profile, name='profile'),
#     path('login/', login_view, name='login'),