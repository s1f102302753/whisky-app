from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse

# Create your views here.

def root(request):          #コントローラ
    return HttpResponse('Hello Django')

#Reactがデータを取得するためのAPI
def quiz_list(request):
    data = {
        "quizzes": [
            {"id": 1, "question": "What is whisky?", "answer": "A distilled beverage."},
            {"id": 2, "question": "Where is Scotch whisky made?", "answer": "Scotland."},
        ]
    }
    return JsonResponse(data)