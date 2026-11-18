from django.contrib.auth.views import LogoutView
from django.urls import path
from .views import HouseKeepLoginView, SignUpView, profile

app_name = 'accounts'
urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path('login/', HouseKeepLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('profile/', profile, name='profile'),
]
