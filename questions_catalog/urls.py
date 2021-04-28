from django.urls import path
from . import views

from questions_catalog.views import user_answers, set_answer, active_polls

urlpatterns = [
    path('polls-list/', active_polls),
    path('answer-list/', user_answers),
    path('set-answer/', set_answer)
]

