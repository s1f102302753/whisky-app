from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse

from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Question, UserScore
from .serializers import QuestionSerializer, UserScoreSerializer

# Create your views here.

def root(request):          #コントローラ
    return JsonResponse({'message': 'API is running'})

# 問題一覧API
class QuizListView(APIView):
    def get(self, request):
        questions = Question.objects.all()
        serializer = QuestionSerializer(questions, many=True)
        return Response({"quizzes": serializer.data})

# スコア情報API
class UserScoreView(APIView):
    def post(self, request):
        serializer = UserScoreSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Score saved successfully"})
        return Response(serializer.errors, status=400)
