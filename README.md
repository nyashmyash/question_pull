Заполнение данных через админку
http://127.0.0.1:8000/admin/
user admin, pass admin

Запускается просто копированием папки где в базе уже применены миграции.
python manage.py runserver

для получения списка всех активных опросов:
http://127.0.0.1:8000/questions_catalog/polls-list/

для получения ответов на вопросы у конкретного пользователя:
http://127.0.0.1:8000/questions_catalog/answer-list/?id_user=1

для проверки вставки запрос через Python:
http://127.0.0.1:8000/questions_catalog/set-answer/

url = 'http://127.0.0.1:8000/questions_catalog/set-answer/'

варианты вызовов для текстовых ответов:
x = requests.post(url, data = '{"id_user": "2", "id_question": "1", "type": "T", "answer_text":"qwer"}')

с одним вариантом:
x = requests.post(url, data = '{"id_user": "2", "id_question": "1", "type": "S", "answer_choice_no": "1"}')

с несколькими:
x = requests.post(url, data = '{"id_user": "2", "id_question": "1", "type": "M", "answer_choice_list": ["1", "2"]}')

id_user - id пользователя
id_question - id вопроса
type - тип 
T - текстовый
S - с одним вариантом
M - с несколькими
answer_text - текст ответа
answer_choice_no - номер по порядку ответа для вопроса с одним вариантом
answer_choice_list - номер по порядку ответов для вопроса с несколькими вариантами

проверки не делаются, надо соблюдать правильность json файла на фронте