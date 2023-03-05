from django.core.exceptions import PermissionDenied  #gives yellow error page
from django.shortcuts import HttpResponse

def only_superuser(func):
    def wrap(request,*args, **kwargs):
        if request.user.is_superuser:
            return func(request,*args, **kwargs)
        else:
            return HttpResponse("<h1>403 Forbidden</h1>")
    return wrap