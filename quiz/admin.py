from django.contrib import admin
from . import models

# Register your models here.

@admin.register(models.Category)

class CatAdmin(admin.ModelAdmin):
    list_display = [
        'name',
    ]

@admin.register(models.Quizzes)

class QuizAdmin(admin.ModelAdmin):
    list_display = [
        'id', 
        'title',
    ]

class AnswerInlineModel(admin.TabularInline):
    model = models.Answer
    fields = [
        'answer_text',
        'is_right'
    ]