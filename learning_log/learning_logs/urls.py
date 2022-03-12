from django.urls import path

from . import views

app_name = 'learning_logs'
urlpatterns = [
    path('', views.index, name='index'),
    path('topics/', views.topics_page, name='topics'),
    path('topics/<int:topic_id>/', views.topic_page, name='topic')
]
