from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='index'),
    path('about-us', views.aboutus, name='aboutus'),
    path('blog', views.blog, name='blog'),
    path('contact-us', views.contact, name='contact'),
    path('services', views.services, name='services'),
    path('subscribe/', views.subscribe, name='subscribe'),
]