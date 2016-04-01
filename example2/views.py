# from django.http import HttpResponse , HttpResponseRedirect
# from django.shortcuts import render , get_object_or_404
# from django.template import loader
# from example2.models import Questions , Choice
# from django.core.urlresolvers import reverse
#
# # Create your views here.
#
# def all_Questions(request):
#     questions_list = Questions.objects.order_by()[:20]
#     return render(request , 'testfile.html' , {'questions_list':questions_list})
#
#
# def detail(request , question_id):
#     question = get_object_or_404(Questions, pk=question_id)
#     return render(request , 'polls/detail.html', {'question': question})
#
# def results(request, question_id):
#     question  = get_object_or_404(Questions , pk=question_id)
#     return render(request , 'polls/results.html' ,
#                   {'question':question})
#
# def vote(request , question_id):
#     question = get_object_or_404(Questions , pk=question_id)
#     try:
#         selected_choice = question.choice_set.get(pk=request.POST['choice'])
#     except(KeyError , Choice.DoesNotExist):
#         context = {'error_message': 'you dident select a correct choice',
#                    'question': question}
#         return render(request , 'polls/detail.html' , context)
#     else:
#         selected_choice.vote += 1
#         selected_choice.save()
#         return HttpResponseRedirect(reverse('results' , args=(question_id)))
#
# def index(request):
#     latest_question_list = Questions.objects.order_by('-pub_date')[:5]
#     context = {'latest_question_list' :latest_question_list}
#     template = loader.get_template("polls/index.html")
#     return HttpResponse(template.render(context , request))

from .models import Questions , Choice
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.shortcuts import get_object_or_404
# from django.views import generic
#
# class IndexView(generic.ListView):
#     template_name = 'polls/index.html'
#     context_object_name = 'latest_question_list'
#
#










