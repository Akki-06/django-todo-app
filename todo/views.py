from  django . shortcuts  import  render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from todo import models
from django.contrib import messages
from django.contrib.auth.decorators import login_required

def signup(request):
    if request.method=='POST':
        fnm = request.POST.get('fnm')
        emailid = request.POST.get('emailid')
        pwd = request.POST.get('pwd')
        
        my_user = User.objects.create_user(fnm, emailid, pwd)
        return redirect('/login')

    return render(request, 'signup.html')

def loginn(request):
    if request.method=='POST':
        fnm = request.POST.get('fnm')
        pwd = request.POST.get('pwd')
        
        user = authenticate(request, username=fnm, password=pwd)
        if user is not None:
            login(request,user)
            return redirect('/todo')
        else:
            messages.error(request, "Invalid username or password")
            return render(request, 'login.html')
        
    return render(request, 'login.html')

@login_required(login_url='/login')
def todo(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        models.TODO.objects.create(title=title,user=request.user)
        return redirect('/todo')

    res = models.TODO.objects.filter(user=request.user).order_by('-date')
    return render(request, 'todo.html', {'res': res})

@login_required(login_url='/login')
def edit_todo(request, srno):
    obj = models.TODO.objects.get(srno=srno)

    if request.method == 'POST':
        obj.title = request.POST.get('title')
        obj.save()
        return redirect('/todo')

    return render(request, 'edit_todo.html', {'obj': obj})

@login_required(login_url='/login')
def delete_todo(request,srno):
    obj = models.TODO.objects.get(srno=srno)
    obj.delete()
    return redirect('/todo')


def signout(request):
    logout(request)
    return redirect('/login')




