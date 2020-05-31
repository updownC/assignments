from django.shortcuts import render, redirect
from .models import Todo, Comment
from django.contrib.auth.models import User
from django.contrib import auth 
from django.contrib.auth.decorators import login_required
# Create your views here.
def home(request):
    todos = Todo.objects.all().order_by('due')
    return render(request, 'home.html', {'todos':todos})

@login_required(login_url="/registration/login")
def new(request):
    if request.method == 'POST':
        new_todo = Todo.objects.create(
            title=request.POST['title'],
            content=request.POST['content'],
            due=request.POST['due'],
            author = request.user
        )
        return redirect('detail', new_todo.pk)
    return render(request, 'new.html')

def detail(request, pk):
    todo=Todo.objects.get(pk=pk)

    if request.method == "POST":
        Comment.objects.create(
            post = todo,
            content = request.POST['content'],
            author = request.user
        )
        return redirect('detail', pk)

    return render(request, 'detail.html', {'todo':todo})

def edit(request, pk):
    todo = Todo.objects.get(pk=pk)
    if request.method == 'POST':
        Todo.objects.filter(pk=pk).update(
            title=request.POST['title'],
            content=request.POST['content'],
            due=request.POST['due']
        )
        return redirect('detail', pk)
    return render(request, 'edit.html', {'todo':todo})

def delete(request, pk):
    todo = Todo.objects.get(pk=pk)
    todo.delete()
    return redirect('home')

def delete_comment(request, pk, comment_pk):
    comment = Comment.objects.get(pk=comment_pk)
    comment.delete()
    return redirect('detail', pk)

def signup(request):
    if request.method == 'POST':
        found_user= User.objects.filter(username=request.POST['username'])
        if len(found_user)>0:
            error='username이 이미 존재합니다'
            return render(request, 'registration/signup.html', {'error':error})
        new_user = User.objects.create_user(
            username=request.POST['username'],
            password=request.POST['password']
        )
        auth.login(request, new_user, backend='django.contrib.auth.backends.ModelBackend')
        return redirect('home')
    return render(request, 'registration/signup.html')

def login(request):
    if request.method == 'POST':
        found_user = auth.authenticate(
            username=request.POST['username'],
            password=request.POST['password']
        )
        if found_user is None:
            error = 'This user does not exist'
            return render(request, 'registration/login.html', {'error':error})
        
        auth.login(request, 
        found_user,
        backend='django.contrib.auth.backends.ModelBackend'
        )
        return redirect(request.GET.get('next','/'))
    return render(request, 'registration/login.html')

def logout(request):
    auth.logout(request)
    return redirect('home')

def mypage(request):
    todos = Todo.objects.all()
    return render(request, 'mypage.html', {'todos':todos})

