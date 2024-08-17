from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('foundation/', views.foundation, name='foundation'),
    path('robot_series/', views.robot_series, name='robot_series'),
]
