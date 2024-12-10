from django.urls import path
from . import views

urlpatterns = [
    path('', views.root, name='root'),
    path('api/quizzes/', views.quiz_list, name='quiz_list'),
]