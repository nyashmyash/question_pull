from django.urls import path
from . import views

from questions_catalog.views import PollsListView, user_answers, set_answer

urlpatterns = [
    path('polls-list/', PollsListView.as_view(template_name="list-polls.html")),
    path('answer-list/', user_answers),
    path('set-answer/', set_answer)
]

