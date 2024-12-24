from . import views
from django.urls import path
from .views import get_question, submit_answer, root


urlpatterns = [
    path('', root),  # ルート
    path('question/<int:question_id>/', views.get_question, name='get_question'),  # 問題一覧API
    path('user-scores/', views.submit_answer, name='submit_answer'), # スコア情報API
]