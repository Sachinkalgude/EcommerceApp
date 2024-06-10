from django.urls import path,include
from .views import *
urlpatterns = [
    path('singup/',signup,name="signup"),
    path('login/',loginView,name="login"),
    path('profile/',profile,name="profile"),
    path('logout/',logoutView,name="logout")
]