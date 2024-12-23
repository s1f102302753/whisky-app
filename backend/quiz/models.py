from django.db import models # type: ignore

# Create your models here.

# 問題
class Question(models.Model):
    question_text = models.CharField(max_length=225)
    explanation = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.question_text
    
# 答え
class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name="answers")
    answer_text = models.CharField(max_length=225)
    is_correct = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.answer_text} (Correct: {self.is_correct})"
    
# ユーザースコア
class UserScore(models.Model):
    user = models.CharField(max_length=225)   # ユーザー名やIDを保存
    score = models.IntegerField(default=0)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user} - {self.score} points"
