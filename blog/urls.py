from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('post/<int:pk>/', views.show_post, name='show_post'),
    path('post/new/', views.create_post, name='create_post'),
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
]