from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='blog-home'),
    path('blog/<slug:slug>/', views.post_details),
    path('about/', views.about, name='blog-about'),
    #path('mydebug/', views.mydebug, name='mydebug')

]
