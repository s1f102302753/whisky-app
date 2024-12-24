from django.contrib import admin # type: ignore
from .models import Category, Question, Choice, UserAnswer, UserScore

# Register your models here.

# 管理画面へモデル登録
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description')

@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ('id', 'text', 'category', 'difficulty', 'explanation')

@admin.register(Choice)
class ChoiceAdmin(admin.ModelAdmin):
    list_display = ('id', 'question', 'text', 'is_correct')

@admin.register(UserAnswer)
class UserAnswerAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'question', 'selected_choice', 'is_correct', 'answered_at')

@admin.register(UserScore)
class UserScoreAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'score', 'date')