���������� ������ ����� �������
http://127.0.0.1:8000/admin/
user admin, pass admin

����������� ������ ������������ ����� ��� � ���� ��� ��������� ��������.
python manage.py runserver

��� ��������� ������ ���� �������� �������:
http://127.0.0.1:8000/questions_catalog/polls-list/

��� ��������� ������� �� ������� � ����������� ������������:
http://127.0.0.1:8000/questions_catalog/answer-list/?id_user=1

��� �������� ������� ������ ����� Python:
http://127.0.0.1:8000/questions_catalog/set-answer/

url = 'http://127.0.0.1:8000/questions_catalog/set-answer/'

�������� ������� ��� ��������� �������:
x = requests.post(url, data = '{"id_user": "2", "id_question": "1", "type": "T", "answer_text":"qwer"}')

� ����� ���������:
x = requests.post(url, data = '{"id_user": "2", "id_question": "1", "type": "S", "answer_choice_no": "1"}')

� �����������:
x = requests.post(url, data = '{"id_user": "2", "id_question": "1", "type": "M", "answer_choice_list": ["1", "2"]}')

id_user - id ������������
id_question - id �������
type - ��� 
T - ���������
S - � ����� ���������
M - � �����������
answer_text - ����� ������
answer_choice_no - ����� �� ������� ������ ��� ������� � ����� ���������
answer_choice_list - ����� �� ������� ������� ��� ������� � ����������� ����������

�������� �� ��������, ���� ��������� ������������ json ����� �� ������