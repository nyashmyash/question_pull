from django.db import models

TYPES = (
    ('T', 'Text answer'),
    ('S', 'Single answer'),
    ('M', 'Many answers'),
)

class User(models.Model):
    name = models.CharField(max_length=200)

class Polls(models.Model):
    poll_name = models.CharField(max_length=200)
    date_start = models.DateTimeField('date start')
    date_end = models.DateTimeField('date end')
    description = models.CharField(max_length=200)
    is_active = models.BooleanField(default=True)

class Question(models.Model):
    poll = models.ForeignKey(Polls, on_delete=models.CASCADE)
    type = models.CharField(max_length=1, choices=TYPES)
    question_text = models.CharField(max_length=200)

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200, default="")
    choice_no = models.PositiveIntegerField(default=0)

class Answer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.DO_NOTHING)
    choice = models.ManyToManyField(Choice)
    answer_text = models.CharField(max_length=1000, default="")