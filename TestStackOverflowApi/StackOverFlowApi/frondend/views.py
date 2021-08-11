import json
from django.shortcuts import render
from search_app.models import Question
from django.core.paginator import Paginator
from .filters import QuestionFilter
import requests



def search(request):
    
    # res = requests.get('http://127.0.0.1:8000/stack/questions/').json()

    questions = Question.objects.all()
    myFilter = QuestionFilter(request.GET, queryset=questions)
    questions = myFilter.qs

    paginator = Paginator(questions, 10)
    page_number = request.GET.get('page', 1)
    ques = paginator.get_page(page_number)
    return render(request, 'search.html', {'ques':ques, 'myFilter':myFilter})
