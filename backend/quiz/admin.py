from django.contrib import admin # type: ignore
from .models import Question, Answer, UserScore

# Register your models here.

# 管理画面へモデル登録
admin.site.register(Question)
admin.site.register(Answer)
admin.site.register(UserScore)
