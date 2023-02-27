from django.shortcuts import render
from django.shortcuts import render, HttpResponse, redirect
from .models import *
from django.contrib.auth.models import User
import re
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
# Create your views here.
from django.contrib.auth.decorators import login_required
from django.core.validators import EmailValidator
from django.core.exceptions import ValidationError
from .models import *
from django.shortcuts import get_object_or_404, render
# from django.utils.translation import gettext_lazy as _
from datetime import datetime

def submit_timer(request):
  if request.method == 'POST':
    # get the submit time from the form data
    submit_time_str = request.POST.get('submit_time', None)
    if submit_time_str is not None:
      # parse the submit time as a datetime object
      submit_time = datetime.strptime(submit_time_str, '%Y-%m-%d %H:%M:%S.%f')
      # save the submit time to the database
      # TODO: replace with your own code to save the submit time to the database
      return HttpResponse('Timer submitted at {}'.format(submit_time))
  return redirect('home')



@login_required(login_url='login')
def home(request):
    context = {
        "user": request.user
    }

    if request.method == "POST":
        checkbox = request.POST.get("checkbox")
        if checkbox == "checked":
            return redirect("questions")
        else:
            messages.error(request, "Checkbox not checked")

    return render(request, "app1/home.html", context)


def userLogin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)

        # if user is not None:
        #     login(request, user)
        #     if request.user.is_superuser:
        #         return redirect("settingwale")
        #     if not (Player.objects.filter(user=request.user).exists()):
        #         print(request.user)
        #         player = Player(user=request.user)
        #         player.save()
        if user is not None:
            login(request, user)
            return redirect("home")
        else:
            messages.error(request, "Login Failed due to invalid credentials!")
            return redirect("login")
            # obj  = Player.objects.filter(user=request.user).exists()
            # print(obj)  #false

            # try:
            #     obj  = Player.objects.filter(user=request.user).exists
            #     # if obj is None:
            #         obj.save()
    return render(request, 'app1/login.html')


def userLogout(request):
    logout(request)
    return redirect("login")


def userRegister(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        rep_password = request.POST['rep_password']
        email = request.POST['email']

        if User.objects.filter(username = username).exists():
            messages.error(request, "User already exists!")
            return redirect("register")
        elif User.objects.filter(email=email).exists():
            messages.error(request, "Email already exists!")
            return redirect("register")
        else:
            if password == rep_password and len(username)>3 and len(password)>8: 
                if re.search('[A-Z]', password)!=None and re.search('[0-9]', password)!=None and re.search("^.*(?=.{8,})(?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[@#$%^&+=]).*$", password)!=None:
                    user = User.objects.create_user(username = username, email = email, password = password)
                    user.save()
                    messages.success(request, "User creation successful! Kindly proceed for login")
                    return redirect("login")
                else:
                    messages.error(request, "Password should contain Uppercase letter")
                    messages.error(request, "Password should contain Lowercase letter")
                    messages.error(request, "Password should contain numbers")
                    messages.error(request, "Password should contain special letters")
                    return redirect("register")
            else:
                messages.error(request, "Length of username > 3")
                messages.error(request, "Length of password > 8")
                messages.error(request, "Entered password = Repeated password")
                return redirect("register")
    return render(request, 'app1/register.html')


@login_required(login_url='login')
def questions(request):
    questions = Question.objects.all()

    return render(request, "app1/questions.html", {"questions": questions})


@login_required(login_url='login')
def question(request, id):
    question = Question.objects.get(q_id=id)
    # testcases = Testcases.objects.get(t_id=id)
    return render(request, "app1/question.html", {"question": question})


@login_required(login_url='login')
def testcases(request, id):
    testcases = Testcases.objects.get(t_id=id)
    return render(request, "app1/question.html", {"question": question})

@login_required(login_url='login')
def settingwale(request):
    context = {}
    players = Player.objects.all()
    users = User.objects.all()
    context["players"] = players
    context["users"] = users
    return render(request, "app1/settingwale.html", context)


@login_required(login_url='login')
def timer_view(request):
    context = {
        'duration': 60,  # duration of timer in seconds
    }
    return render(request, 'timer.html', context)


# function updateTimer() {
#     var now = new Date().getTime()
#     var remaining = duration - Math.floor((now - startTime) / 1000)
#     if (remaining < 0) {
#         remaining = 0
#     }
#     document.getElementById('timer').innerHTML = remaining
#     if (remaining > 0) {
#         setTimeout(updateTimer, 1000)
#     } else {
#         // timer has ended, send update to server
#         $.ajax({
#             type: 'POST',
#             url: '/timer/update/',
#             data: {'time_up': true},
#             success: function(data) {
#                 console.log('Timer updated successfully')
#             }
#         })
#     }
# }




