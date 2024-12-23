from . import views
from django.urls import path
from .views import QuizListView, UserScoreView, root


urlpatterns = [
    path('', root),  # ルート
    path('quizzes/', QuizListView.as_view(), name='quiz-list'),  # 問題一覧API
    path('user-scores/<int:pk>/', QuizListView.as_view(), name='quiz-score'), # スコア情報API
]