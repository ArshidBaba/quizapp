# from django.contrib import admin
# from . import models

# # Register your models here.

# @admin.register(models.Category)

# class CatAdmin(admin.ModelAdmin):
#     list_display = [
#         'name',
#     ]

# @admin.register(models.Quizzes)

# class QuizAdmin(admin.ModelAdmin):
#     list_display = [
#         'id', 
#         'title',
#     ]

# class AnswerInlineModel(admin.TabularInline):
#     model = models.Answer
#     fields = [
#         'answer_text',
#         'is_right'
#     ]

# @admin.register(models.Question)

# class QuestionAdmin(admin.ModelAdmin):
#     fields = [
#         'title',
#         'quiz',
#     ]
#     list_display = [
#         'title',
#         'quiz',
#         'date_updated'
#     ]

#     inlines = [
#         AnswerInlineModel,
#     ]


from django.contrib import admin
from . import models

admin.site.register(models.Category)
admin.site.register(models.Quizzes)
admin.site.register(models.Question)
# admin.site.register(BookInstance)