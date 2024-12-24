from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from .models import Question, Choice, UserAnswer, UserScore
from django.contrib.auth.models import User

def root(request):
    return JsonResponse({'message': 'Hello, World!'})

# 問題と選択肢を返すAPI
def get_question(request, question_id):
    question = get_object_or_404(Question, id=question_id)
    choices = Choice.objects.filter(question=question)
    
    question_data = {
        "id": question.id,
        "text": question.text,
        "choices": [
            {"id": choice.id, "text": choice.text} for choice in choices
        ],
        "explanation": question.explanation
    }
    
    return JsonResponse(question_data)

# ユーザーの回答を保存するAPI
def submit_answer(request):
    user = request.user
    question_id = request.POST.get('question_id')
    choice_id = request.POST.get('choice_id')
    
    question = get_object_or_404(Question, id=question_id)
    choice = get_object_or_404(Choice, id=choice_id)
    
    is_correct = choice.is_correct
    user_answer = UserAnswer.objects.create(
        user=user,
        question=question,
        selected_choice=choice,
        is_correct=is_correct
    )
    
    # スコアの更新
    score, created = UserScore.objects.get_or_create(user=user)
    if is_correct:
        score.score += 10
    score.save()
    
    return JsonResponse({
        'is_correct': is_correct,
        'explanation': question.explanation
    })
