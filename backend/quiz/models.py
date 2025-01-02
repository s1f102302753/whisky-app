from django.db import models # type: ignore
from django.contrib.auth.models import User

# Create your models here.

# カテゴリー
class Category(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.name

# 問題
class Question(models.Model):
    text = models.CharField(max_length=225)
    category = models.ForeignKey(
        'category',  # アプリ名.モデル名
        on_delete=models.CASCADE,
        default=1
    )
    difficulty = models.IntegerField(
        choices=[
            (1, 'Hard'),
            (2, 'Medium'),
            (3, 'Easy'),
        ],
        default=3,
    )
    explanation = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.text
    
# 選択肢
class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='choices')
    text = models.CharField(max_length=255)
    is_correct = models.BooleanField(default=False)

    def __str__(self):
        return self.text
    
class UserAnswer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    selected_choice = models.ForeignKey(Choice, on_delete=models.CASCADE)
    is_correct = models.BooleanField()
    answered_at = models.DateTimeField(auto_now_add=True)

# ユーザースコア
class UserScore(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    score = models.IntegerField(default=0)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user} - {self.score} points"
