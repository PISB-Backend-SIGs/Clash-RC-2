from django.shortcuts import render,HttpResponse, redirect
from django.http import JsonResponse
from .models import *
from django.contrib.auth.models import User
import re
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
# Create your views here.
from django.contrib.auth.decorators import login_required
from .utils import *
from .models import *
from .decorators import (only_superuser)
from .runner_utils import runCode

@login_required(login_url='login')
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
            try:
                player = Player.objects.get(user=user)
                if not(player.p_is_loged_in):
                    login(request, user)
                    player.p_is_loged_in = True
                    player.save()
                else:
                    messages.error(request, "You are already login")
                    return redirect("login")
            except:
                player=Player(user=user,p_is_loged_in=True)
                player.save()
                login(request, user)

            # if request.user.is_superuser:         #to direct login to admin pannel
            #     return redirect("settingwale")
            
            # if not(Player.objects.filter(user=request.user).exists()):
            #     print(request.user)
            #     player=Player(user=request.user)
            #     player.save()
            

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
    user = User.objects.get(username=request.user)
    player = Player.objects.get(user=user)
    team = Team.objects.get(user__username=request.user)
    print("team ",team)
    context["question"]=question
    context["player"]=player
    context["team"]=team

    try:
        submission = Submission.objects.filter(player=user,q_id=question,q_status="AC").last()
        # print("subtry",submission[0].s_code)
        # print("subtry",submission)
        # print("subtry",submission[0].s_code)
        context["user_code"]=submission.s_code

    except:
        try:
            submission = Submission.objects.filter(player=user,q_id=question).last()
            context["user_code"]=submission.s_code
        except:
            context["user_code"]=""
    try:
        if submission.s_language == "cpp":
            context["code_lang_cpp"]="cpp"
        if submission.s_language == "c":
            context["code_lang_c"]="c"
    except:
        pass
    return render(request,"app1/question.html",context)

@login_required(login_url='login')
def question_sub(request,id):
    print("inside question_sub ")
    context={}
    question = Question.objects.get(q_id=id)
    user = User.objects.get(username = request.user)
    team = Team.objects.get(user =user)
    if request.method=="POST":
        print("question_sub inside post")
        user_code = request.POST.get("user_code")
        language = request.POST.get("code_lang")
        btn_status = int(request.POST.get("btn_clicked"))
        
        print("users code :",user_code,"languageddddddd 0",language,"stat : ",type(btn_status))

        if (btn_status==0):
            print("run clciked")
            user_test_ip = request.POST.get("testip")
            status = runCode(id,user_code,language,btn_status,user_test_ip)

            dict = {
                "status":1,
                "tc_count":status,
                "testip":user_test_ip,
                "testop":status[0],
            }
            return JsonResponse(dict)

        submission = Submission(team=team,player=user,q_id=question,s_code=user_code,s_language=language)
        

        status = runCode(id,user_code,language,btn_status,"No")
        if (status.count("AC")==len(status)):
            submission.q_status = "AC"
        else:
            submission.q_status = "WA"
        submission.save()

        # return redirect(f"/question/{id}")
        return JsonResponse({"status":1,"tc_count":status})

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


# from django.contrib.auth.decorators import user_passes_test
# @user_passes_test(lambda u: u.is_superuser)
@only_superuser
@login_required(login_url='login')
def settingwale(request):
    context={}
    players = Player.objects.all()
    users = User.objects.all()
    context["players"]=players
    context["users"]=users
    return render(request,"app1/settingwale.html",context)


def test(request):
    if (request.method == "POST"):
        return JsonResponse({"status":1})
    else:
        return JsonResponse({"status":0})
    # make_dir("prasad")
    return render(request,"app1\\test.html")