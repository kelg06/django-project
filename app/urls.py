from django.urls import path
from app.views import *

urlpatterns = [
    path('signup', signup, name='register'),
    path('login', loginPage ,name='login'),
    path('logout', logoutUser ,name='logout'),
    path('', index,name='home'),
    path('add/',add,name='add'),
    path('favorites/',fav,name="fav"),
    path('about',about,name='about') ,
    path('topic',topic,name='topic')   
]
