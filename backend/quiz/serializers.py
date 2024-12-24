from rest_framework import serializers # type: ignore
from .models import Category, Question, Choice, UserAnswer, UserScore

# 選択肢
class ChoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Choice
        fields = ['id', 'text', 'is_correct']

# 問題シリアライザ
class QuestionSerializer(serializers.ModelSerializer):
    answers = ChoiceSerializer(many=True, read_only=True)

    class Meta:
        model = Question
        fields = ['id', 'text', 'category', 'difficulty', 'explanation', 'answers']

# ユーザースコアシリアライザ
class UserScoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserScore
        fields = ['id', 'user', 'score', 'date']
