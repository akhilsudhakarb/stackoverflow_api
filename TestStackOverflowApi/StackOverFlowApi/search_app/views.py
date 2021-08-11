from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import viewsets
from .models import Question
from .serializer import QuestionSerializer
from bs4 import BeautifulSoup
from .import throttle

import requests
import json



class QuestionApi(viewsets.ModelViewSet):
    
    throttle_classes = [throttle.AnonMinThrottle, throttle.AnonDayThrottle]
    serializer_class = QuestionSerializer
    queryset = Question.objects.all()

    def latest(request):
        try:
            res = requests.get('https://stackoverflow.com/questions')
            print(res)
            soup = BeautifulSoup(res.text, 'html.parser')
            question = soup.select('.question-summary')
            for ques in question:

                q = ques.select_one('.question-hyperlink').getText()
                vote_count = ques.select_one('.vote-count-post').getText()
                views = ques.select_one('.views').attrs['title']
                tags = [i.getText() for i in (ques.select('.post-tag'))]

                question = Question()
                question.questions = q
                question.vote_count = vote_count
                question.views = views
                question.tags = tags
                question.save()
            return HttpResponse('Latest data fetched')
        except e as Exception:
            return HttpResponse(f'Failed to fetch {e}')



def index(request):

    return HttpResponse('success')
