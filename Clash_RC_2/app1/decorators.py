from django.core.exceptions import PermissionDenied  #gives yellow error page
from django.shortcuts import HttpResponse
import app1.views
from django.contrib.auth.models import User
from .models import Player, Contest_time
from datetime import date, timedelta, datetime
from django.utils import timezone
from django.shortcuts import redirect

def only_superuser(func):
    def wrap(request,*args, **kwargs):
        if request.user.is_superuser:
            return func(request,*args, **kwargs)
        else:
            return HttpResponse("<h1>403 Forbidden</h1>")
    return wrap


def check_time(view_fun):
    def wrap(request,*args, **kwargs):
        print("inside dec username",request.user)
        user = User.objects.get(username=request.user)
        # player = Player.objects.get(user= user)
        contest_time = Contest_time.objects.all()
        end_time = contest_time[0].end_time.astimezone()
        end_time = datetime(year=end_time.year, month=end_time.month, day=end_time.day, hour=end_time.hour, minute=end_time.minute, second=end_time.second)
        final_time = int(end_time.timestamp())   #user end time in sec
        current_time =  int(datetime.now().timestamp())   #crrent server time in sec
        print("end time ",final_time,end_time)
        print("crnt time ",current_time,datetime.now())
        print("diff ",final_time-current_time)
        dif = final_time-current_time

        if (dif < 0):
            return app1.views.leaderboard(request)
            # return view_func(request,*args,**kwargs)
        else:
            return view_fun(request,*args,**kwargs)
        # return view_fun(request,*args,**kwargs)            
    return wrap

def check_test_ended(view_fun):
    def wrap(request,*args,**kwargs):
        if (request.user.is_authenticated):
            user = User.objects.get(username=request.user)
            player = Player.objects.get(user= user)
            if (player.p_is_ended):
                print("game is ended")
                print("iside decoratro to check going result in testcheck")

                return app1.views.result(request)
                # return redirect('result')
            else:
                print("game is not ended")

                return view_fun(request,*args,**kwargs)
        else:
            # return app_1.views.signin(request)
            return redirect("signin")
    return wrap