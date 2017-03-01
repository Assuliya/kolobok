from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib import messages

def index(request):
    if request.method == "GET":
        return render(request, 'kolobok_story/index.html')
    if request.method == "POST":
        answers = ['d','a','d','b','b','c']
        result = []
        count = 0
        for idx, val in enumerate(answers):
            question_num = idx + 1
            if request.POST[str(question_num)] == val:
                dic = {'number':question_num, 'check': 'Right'}
                count += 1
            else:
                dic = {'number':question_num, 'check': 'Wrong'}
            result.append(dic)
        context = {'result':result, 'count':count}
        return render(request, 'kolobok_story/index.html', context)
