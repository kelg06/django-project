from django.urls import path
from app.views import *

urlpatterns = [
    path('', index,name='home'),
    path('add/',add,name='add'),
    path('favorites/',fav,name="fav"),
    path('about',about,name='about')    
]
