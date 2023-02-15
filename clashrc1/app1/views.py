from django.shortcuts import render,HttpResponse
from .models import *
# Create your views here.

def home(request):
    return HttpResponse("hekkk")

def questions(request):
    questions = Question.objects.all()

    return render(request,"app1/questions.html",{"questions":questions})

def question(request,id):
    question = Question.objects.get(q_id=id)
    return render(request,"app1/question.html",{"question":question})