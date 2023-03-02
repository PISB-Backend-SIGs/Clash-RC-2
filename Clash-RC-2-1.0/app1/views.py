from django.shortcuts import render,HttpResponse, redirect
from .models import *
from django.contrib.auth.models import User
import re
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
# Create your views here.
from django.contrib.auth.decorators import login_required
from .utils import *
from .models import *


# @login_required(login_url='login')
def home(request):
    context={
        "user":request.user
    }

    if request.method == "POST":
        checkbox = request.POST.get("checkbox")
        if checkbox == "checked":
            return redirect("questions")
        else:
            messages.error(request, "Checkbox not checked")

    return render(request,"app1/home.html",context)

def userLogin(request):
    print("in login")
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        print(username)
        print(password)

        user = authenticate(request, username = username, password = password)
        
        if user is not None:
            login(request, user)
            # if request.user.is_superuser:         #to direct login to admin pannel
            #     return redirect("settingwale")
            if not(Player.objects.filter(user=request.user).exists()):
                print(request.user)
                player=Player(user=request.user)
                player.save()

            # obj  = Player.objects.filter(user=request.user).exists()
            # print(obj)  #false

            # try:
            #     obj  = Player.objects.filter(user=request.user).exists
            #     # if obj is None:
            #         obj.save()
            
            
            return redirect("home")
        else:
            messages.error(request, "Login Failed due to invalid credentials!")
            return redirect("login")
    return render(request, 'app1/login.html')

def userLogout(request):
    logout(request)
    return redirect("login")

def userRegister(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        rep_password = request.POST.get('rep_password')
        email = request.POST.get('email')

        if User.objects.filter(username = username).exists():
            messages.error(request, "User already exists!")
            return redirect("register")
        else:
            if password == rep_password and  len(password)>8: 
                if re.search('[A-Z]', password)!=None and re.search('[0-9]', password)!=None and re.search("^.*(?=.{8,})(?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[@#$%^&+=]).*$", password)!=None:
                    user_registration = User.objects.create_user(username = username, email = email, password = password)
                    user_registration.save()
                    player = Player(user=user_registration)
                    player.save()
                    messages.success(request, "User creation successful! Kindly proceed for login")
                    return redirect("login")
                else:
                    messages.error(request, "Enter valid credentials")
                    return redirect("register")
            else:
                messages.error(request, "User registration failed!")
                return redirect("register")
    return render(request, 'app1/register.html')


@login_required(login_url='login')
def questions(request):
    questions = Question.objects.all()
    user=User.objects.get(username=request.user)
    return render(request,"app1/questions.html",{"questions":questions,"player":user})

@login_required(login_url='login')
def question(request,id):
    context={}
    question = Question.objects.get(q_id=id)
    print("question",question)
    player = Player.objects.get(user=request.user)
    team = Team.objects.get(user__username=request.user)
    print("team ",team)
    context["question"]=question
    context["player"]=player
    context["team"]=team
    try:
        submission = Submission.objects.filter(team=team,q_id=question,q_status="AC").last()
        # print("subtry",submission[0].s_code)
        # print("subtry",submission)
        # print("subtry",submission[0].s_code)
        context["user_code"]=submission.s_code
    except:
        try:
            submission = Submission.objects.filter(team=team,q_id=question).last()
            context["user_code"]=submission.s_code
        except:
            context["user_code"]=""
        # print(submission)
        # submission = Submission.objects.all()
        # print("sub",submission)
        # print("sub",submission[8].q_status)
        # print(submission[0])
        # print(submission[0].s_code)
        # context["user_code"]=submission.s_code

    return render(request,"app1/question.html",context)

@login_required(login_url='login')
def question_sub(request,id):
    print("inside question_sub ")
    context={}
    question = Question.objects.get(q_id=id)
    team = Team.objects.get(user__username=request.user)
    if request.method=="POST":
        print("question_sub inside post")
        user_code = request.POST.get("user_code")
        submission = Submission(team=team,q_id=question,s_code=user_code)
        submission.save()
        test_cases = Testcases.objects.filter(q_id=id)
        context["user_code"]=user_code
        context["test_cases"]=test_cases
        return render(request,"app1/question.html",context)

# @login_required(login_url='login')
def leaderboard(request):
    context={
        "title":"Result"
    }
    # team1 =Team.objects.all().values()  #to check attributes
    # print(team1)
    team =Team.objects.all().order_by('-team_score')
    # print(team)
    user=User.objects.all()
    # print(user.filter(team__id=3)[0].username)
    dict=get_leaderboard(team,user)   #to get list of dictionary containing places of users 
    # team2 =User.objects.filter()

    context["teams"]=dict
    return render(request,"app1/result.html",context)


@login_required(login_url='login')
def settingwale(request):
    context={}
    players = Player.objects.all()
    users = User.objects.all()
    context["players"]=players
    context["users"]=users
    return render(request,"app1/settingwale.html",context)

