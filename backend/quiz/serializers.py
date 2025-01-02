from rest_framework import serializers # type: ignore
from .models import Question, Choice, UserAnswer, UserScore

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


# ユーザ情報
class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        models = User
        fields = ['username', 'password', 'email']

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            password=validated_data['password'],
            email=validated_data['email', '']
        )
        return user

    
