from django.urls import path
from . import views


urlpatterns = [
    path('', views.list, name='list'),
    path('post/<int:pk>/', views.detail, name='detail'),
    path('post/new/', views.new, name='new'),
    path('post/<int:pk>/edit/', views.edit, name='edit'),
]
