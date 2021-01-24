from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse

from .models import *


def index(request):
    question_list = Question.objects.order_by('pub_date')
    context = {'question_list': question_list}
    return render(request, 'poll/index.html', context)  # Shortcut for the two lines below
    # template = loader.get_template('poll/index.html')
    # return HttpResponse(template.render(context, request))
    # output = ', '.join(q.question_text for q in question_list)
    # return HttpResponse(output)


def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    context = {'question': question}
    return render(request, 'poll/detail.html', context)
    # return HttpResponse(f"You are looking at question Number {question_id}")


def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'poll/results.html', {'question': question})


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    selected_choice = question.choice_set.get(pk=request.POST['choice'])

    selected_choice.votes += 1
    selected_choice.save()
    return HttpResponseRedirect(reverse('poll:results', args=(question_id,)))

