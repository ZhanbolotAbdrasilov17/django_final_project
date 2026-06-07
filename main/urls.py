from django.urls import path
from setuptools.extern import names

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('blog/', views.blog, name='blog'),
    path('blog/<int:pk>/', views.blog_single, name='blog_single'),
    path('contact/', views.contact, name='contact'),
    path('course/', views.course, name='course'),

]

