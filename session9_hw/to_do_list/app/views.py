from django.shortcuts import render, redirect
from .models import Todo

# Create your views here.
def home(request):
    todos = Todo.objects.all().order_by('due')
    return render(request, 'home.html', {'todos':todos})

def new(request):
    if request.method == 'POST':
        new_todo = Todo.objects.create(
            title=request.POST['title'],
            content=request.POST['content'],
            due=request.POST['due']
        )
        return redirect('detail', new_todo.pk)
    return render(request, 'new.html')

def detail(request, pk):
    todo=Todo.objects.get(pk=pk)
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

    
