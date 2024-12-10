from django.urls import path
from . import views
from .views import QuizListView, UserScoreView


urlpatterns = [
    path('', views.root, name='root'),
    path('api/v1/quizzes/', QuizListView.as_view(), name='quiz-list'),
    path('api/v1/scores/', UserScoreView.as_view(), name='user-score'),
]