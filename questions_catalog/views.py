
# Create your views here.
from questions_catalog.models import User, Polls, Question, Choice, Answer, TYPES
from django.http import JsonResponse
from django.http import HttpResponse
from datetime import datetime
import json
    

def active_polls(request):
    polls = Polls.objects.filter(date_end__gte=datetime.now(), is_active=True
                    ).order_by('date_start')
    output = []
    for p in polls:
        output.append([p.poll_name, str(p.date_start), str(p.date_end), p.description])
    return HttpResponse(str(output))

from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def set_answer(request):
    try:
        data = json.loads(request.body.decode())
    except ValueError:
        return JsonResponse({
            'error': 'format error'
        })
    id_question=data['id_question']
    id_user = int(data.get("id_user", "0"))
    type_question=data.get('type')
    choices = set()
    _answer_text = ''
    user_lst = User.objects.filter(id=id_user)
    if len(user_lst) == 0:
        user = User(name = "anonim" + str(id_user))
        user.save()
    else:
        user = user_lst[0]
    if type_question == 'T':
        _answer_text=data.get('answer_text','')
    elif type_question == 'S':
        ch_no = int(data.get('answer_choice_no'))
        one_choice = Choice.objects.get(question__id=id_question, choice_no=ch_no)
        choices.add(one_choice)
    elif type_question == 'M':
        choice_no_list = data.get('answer_choice_list')
        for ch_no in choice_no_list:
            one_choice = Choice.objects.get(question__id=id_question, choice_no=int(ch_no))
            choices.add(one_choice)
    answ = Answer.objects.create(user=user, question=Question.objects.get(id=id_question), answer_text=_answer_text)
    for ch in choices:
        answ.choice.add(ch)
    return HttpResponse("answer created")

def user_answers(request):
    id = request.GET.get("id_user", 0)
    list_answ = Answer.objects.filter(user__id=id)
    if len(list_answ) == 0:
        return HttpResponse("any answers don't exists")
    
    output = {}
    output['username'] = User.objects.get(id=id).name
    output['answers'] = {}
    for answer in list_answ:
        poll_name = answer.question.poll.poll_name
        question = [answer.question.id, answer.question.question_text]
        if answer.answer_text!="":
            answer_val = answer.answer_text
        else:
            answer_val = dict()
            for choice in answer.choice.all():
                answer_val[choice.choice_no] = [choice.id, choice.choice_text]
        if output['answers'].get(poll_name)!=None:
            output['answers'][poll_name].append([question, answer_val])
        else:
            output['answers'][poll_name] = [[question, answer_val],]
    return HttpResponse(str(output))
    
