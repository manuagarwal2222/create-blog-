from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('Post/<str:pk>',views.Post, name='Post')
]
