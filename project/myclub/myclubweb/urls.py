from django.urls import path
from . import views

urlpatterns = [
    path('myclubweb/', views.index),
    path('myclubweb/<slug:meetup_slug>', views.meetups_details),
]