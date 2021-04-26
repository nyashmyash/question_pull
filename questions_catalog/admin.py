from django.contrib import admin
from questions_catalog.models import Polls, User, Question, Answer, Choice

class PollsAdmin(admin.ModelAdmin):
    fields = ('poll_name', 'date_start', 'date_end', 'description')

class QuestionAdmin(admin.ModelAdmin):
    fields = ('poll', 'type', 'question_text')

class AnswerAdmin(admin.ModelAdmin):
    fields = ('user', 'question', 'choice', 'answer_text')

class ChoiceAdmin(admin.ModelAdmin):
    fields = ('question', 'choice_text')

class UserAdmin(admin.ModelAdmin):
    fields = ('name', )

admin.site.register(Polls, PollsAdmin)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Answer, AnswerAdmin)
admin.site.register(Choice, ChoiceAdmin)
admin.site.register(User, UserAdmin)