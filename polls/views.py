from django.shortcuts import render
from django.http import HttpResponse
from polls.models import Question, Choice
from django.template import loader
from django.http import Http404
from django.shortcuts import get_object_or_404
# Create your views here.


def index(request):
    # return HttpResponse("hi.......")
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    template = loader.get_template('polls/index.html')
    context = {
		'latest_question_list': latest_question_list,
        	}
    return HttpResponse(template.render(context, request))


def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question': question})


def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/results.html', {'question': question})

def vote(request, question_id):
    question = get_object_or_404(Question, pk = question_id)
    try:
      selected_choice = question.choice_set.get(pl = request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'polls/detail.html',
                      {
                        'question': question,
                        'error_message': "Please select a choice",
                      })
    else:
        selected_choice.votes+=1
        selected_choice.save()


    return HttpResponse("You are voting for question %s." % question_id)
