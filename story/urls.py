from django.urls import path
from . import views


urlpatterns = [
    path('', views.home_page, name='home'),
    path('stories/', views.story_list, name='story_list'),
    path('<slug:title>/', views.chapter_list, name='chapter_list'),
    path('<slug:title>/<int:chapter_number>/', views.chapter, name='chapter')
]