from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('place/', views.place, name='place'),
    path('update/', views.update, name='update'),
    path('getStatus/', views.getStatus, name='getStatus'),
]