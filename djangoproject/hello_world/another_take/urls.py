from django.urls import path
from . import views

urlpatterns = [
    path('HELLO/', views.say_hello, name='HELLO'),

]