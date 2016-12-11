from django.shortcuts import render
from django.http import HttpResponseRedirect


from django.contrib.auth import login, authenticate, get_user_model,logout

from .forms import LoginForm


def login_view(request):
    title= 'Login'
    print(request.user.is_authenticated())
    form = LoginForm(request.POST or None)
    if form.is_valid():
        print('username')
        username = form.cleaned_data.get('username')
        print(username,'username')
        password = form.cleaned_data.get('password')
        user = authenticate(username=username, password=password)
        login(request,user)
        print(request.user.is_authenticated())
        return HttpResponseRedirect('/bofa/home/')
    return render(request,"form.html",{'form':form})

def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/login/')
