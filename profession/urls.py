from django.urls import path
from .views import *
from .import views

app_name = 'profession'


urlpatterns = [
    path('',views.home,name ='home')

]
