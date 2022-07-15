from django.urls import path
from .views import home, annonce, add_annonce, update_annonce, delete_message

# app_name = "events"

urlpatterns = [
    path('', home, name="home"),
    path('add_groupe/', add_annonce, name='add_annonce'),
    path('annonce/<str:pk>', annonce, name="annonce"),
    path('update_annonce/<str:pk>', update_annonce, name="update_annonce"),
    path('delete_message/<str:pk>', delete_message, name="delete_message"),

]