from django.test import TestCase
from datetime import datetime, date
from django.http import HttpRequest
from django.test import Client
from django.test import override_settings
import json

from questions_catalog.models import User, Polls, Question, Choice, Answer

class ApiTestClass(TestCase):

    def setUp(self):
        # Установки запускаются перед каждым тестом
        user = User.objects.create(id=1, name = "test")
        poll = Polls.objects.create(id=1,poll_name="test_poll1", date_start=date(2021, 1, 1), date_end=date(2022, 1, 1), description="test")
        Polls.objects.create(id=2,poll_name="test_poll2", date_start=date(2021, 1, 1), date_end=date(2022, 1, 1), description="test1")
        Polls.objects.create(id=3,poll_name="test_poll3", date_start=date(2021, 1, 1), date_end=date(2022, 1, 1), description="test2")
        question_t = Question.objects.create(id=1, poll=poll, type='T', question_text="question_text1")
        question_s = Question.objects.create(id=2, poll=poll, type='S', question_text="question_text2")
        question_m = Question.objects.create(id=3, poll=poll, type='M', question_text="question_text3")
        Choice.objects.create(id=1, question=question_s,choice_text="asdf", choice_no="1")
        Choice.objects.create(id=2, question=question_s,choice_text="assdf", choice_no="2")
        Choice.objects.create(id=3, question=question_m,choice_text="qwerty", choice_no="1")
        Choice.objects.create(id=4, question=question_m,choice_text="qwrrr", choice_no="2")
        Choice.objects.create(id=5, question=question_m,choice_text="asdf", choice_no="3")
        Answer.objects.create(user=user, question=question_t, answer_text="answer_text")

    def tearDown(self):
        # Очистка после каждого метода
        pass

    def test_get_active_polls(self):
        c = Client()
        response = c.get('/questions_catalog/polls-list/')
        resp_content = response.content.decode()
        expect_content = "[['test_poll1', '2021-01-01 00:00:00', '2022-01-01 00:00:00', 'test'], ['test_poll2', '2021-01-01 00:00:00', '2022-01-01 00:00:00', 'test1'], ['test_poll3', '2021-01-01 00:00:00', '2022-01-01 00:00:00', 'test2']]"
        self.assertTrue(resp_content==expect_content)
    
    def test_get_user_answers(self):
        c = Client()
        response = c.get('/questions_catalog/answer-list/', data={'id_user': 1})
        resp_content = response.content.decode()
        expect_content = "{'username': 'test', 'answers': {'test_poll1': [[[1, 'question_text1'], 'answer_text']]}}"
        self.assertTrue(resp_content==expect_content)

    def test_create_text_answer(self):
        c = Client()
        json_str = '{"id_user": "1", "id_question": "1", "type": "T", "answer_text": "hello"}'
        response = c.post('/questions_catalog/set-answer/', data= json_str, content_type='application/json')
        self.assertTrue(response.content.decode()=="answer created")
        response = c.get('/questions_catalog/answer-list/', data={'id_user': 1})
        resp_content = response.content.decode()
        expect_content = "{'username': 'test', 'answers': {'test_poll1': [[[1, 'question_text1'], 'answer_text'], [[1, 'question_text1'], 'hello']]}}"
        self.assertTrue(resp_content==expect_content)

    def test_create_single_answer(self):
        c = Client()
        json_str = '{"id_user": "1", "id_question": "2", "type": "S", "answer_choice_no": "1"}'
        response = c.post('/questions_catalog/set-answer/', data= json_str, content_type='application/json')
        self.assertTrue(response.content.decode()=="answer created")
        response = c.get('/questions_catalog/answer-list/', data={'id_user': 1})
        resp_content = response.content.decode()
        expect_content = "{'username': 'test', 'answers': {'test_poll1': [[[1, 'question_text1'], 'answer_text'], [[2, 'question_text2'], {1: [1, 'asdf']}]]}}"
        self.assertTrue(resp_content==expect_content)

    def test_create_multi_answer(self):
        c = Client()
        json_str = '{"id_user": "1", "id_question": "3", "type": "M", "answer_choice_list": ["2", "3"]}'
        response = c.post('/questions_catalog/set-answer/', data= json_str, content_type='application/json')
        self.assertTrue(response.content.decode()=="answer created")
        response = c.get('/questions_catalog/answer-list/', data={'id_user': 1})
        resp_content = response.content.decode()
        expect_content = "{'username': 'test', 'answers': {'test_poll1': [[[1, 'question_text1'], 'answer_text'], [[3, 'question_text3'], {2: [4, 'qwrrr'], 3: [5, 'asdf']}]]}}"
        self.assertTrue(resp_content==expect_content)
        

        