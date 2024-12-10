from rest_framework import serializers # type: ignore
from .models import Question, Answer, UserScore

# 問題シリアライザ
class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = ['id', 'answer_text', 'is_correct']

class QuestionSerializer(serializers.ModelSerializer):
    answers = AnswerSerializer(many=True, read_only=True)

    class Meta:
        model = Question
        fields = ['id', 'question_text', 'explanation', 'answers']

# ユーザースコアシリアライザ
class UserScoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserScore
        fields = ['id', 'user', 'score', 'date']
