from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about_html/', views.about_html, name='about_html'),
]
