from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from .models import Question, Choice

import json

# Create your views here.
def index(request):
    question_list = Question.objects.all()
    context = {'question_list': question_list}
    return render(request, 'polls/index.html', context)

def detail(request, question_id):
    question = get_object_or_404(Question, id=question_id)
    return render(request, 'polls/detail.html', {'question': question})

def latest(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'polls/latest.html', context)

def results(request, question_id):
    question = get_object_or_404(Question, id=question_id)
    choices = question.choice_set.all()
    choices_text = [choice.choice_text for choice in choices]
    votes = [choice.votes for choice in choices]
    context = {
        'question': question,
        'choice1': choices_text[0],
        'choice2': choices_text[1],
        'choice3': choices_text[2],
        'choice4': choices_text[3],
        'choices': choices_text,
        'votes': votes,
        }
    return render(request, 'polls/results.html', context)

def about(request):
    context = {}
    return render(request, 'polls/about.html', context)

def createPoll(request):
    context = {}
    return render(request, 'polls/create_poll.html', context)

def newPoll(request):
    data = json.loads(request.body)
    if Question.objects.filter(question_text=data['poll_data']['question']).exists():
        response = "Sorry, but a similar poll already exists!"
    else:
        new_poll = Question.objects.create(question_text=data['poll_data']['question'])
        new_poll.save()
        for choice in data['poll_data']['choices'].values():
            choice = Choice.objects.create(question=new_poll, choice_text=choice)
            choice.save()
        response = "Success, your poll has been created and published."
    return JsonResponse(response, safe=False)

@csrf_exempt
def process_choice(request):
    data = json.loads(request.body)
    choice = Choice.objects.get(id=data['choiceId'])

    choice.votes += 1
    choice.save()

    return JsonResponse("Thank you for voting!", safe=False)