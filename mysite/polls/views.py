from django.shortcuts import render, get_object_or_404
from django.http.response import HttpResponse, HttpResponseRedirect
from django.http import Http404
from django.template import RequestContext, loader
from django.urls import reverse
from django.views import generic
from .models import Question, Choice


'''
def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    # latest_question_list = Question.objects.all()
    # output = ', '.join([q.question_text for q in latest_question_list])
    template = loader.get_template("polls/index.html")
    context = RequestContext(request, {
        'latest_question_list': latest_question_list,
    })
    return HttpResponse(template.render(context))
'''

'''
def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'polls/index.html', context)
'''

class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        '''return the latest five question list'''
        return Question.objects.order_by('-pub_date')[:5]

'''
def detail(request, question_id):
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("question does not exist!")
    return render(request, "polls/detail.html", {'question': question})
'''

'''
def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, "polls/detail.html", {'question': question})
'''
class DetailView(generic.DetailView):
    template_name = 'polls/detail.html'
    model = Question


'''
def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, "polls/results.html", {'question': question})
'''
class ResultsView(generic.DetailView):
    template_name = 'polls/results.html'
    model = Question


def vote(request, question_id):
    q = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = q.choice_set.get(pk=request.POST['choice'])
    except(KeyError, Choice.DoesNotExist):
        return render(request, "polls/detail.html", {
            'question': q,
            'error_message': "You didn't select a choice",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse('polls:results', args=(q.id,)))
