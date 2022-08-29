from django.urls import path
from . import views

urlpatterns=[
    path('',views.home,name="home"),
    path('email_sent/',views.email_sent,name='email_sent')
]