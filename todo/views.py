from django.shortcuts import render,redirect
from .models import *
from .forms import TaskForm
# Create your views here.

def index(request):
    tasks=Task.objects.all()
    form=TaskForm()
    if request.method=='POST':
        form=TaskForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/') 
    return render(request,"todo/index.html",{'tasks':tasks,'form':form})

def update(request,pk):
    task=Task.objects.get(id=pk)
    form =TaskForm(instance=task)
    if request.method=="POST":
        form=TaskForm(request.POST,instance=task)
        if form.is_valid():
            form.save()
        return redirect('/')

    return render(request,"todo/updatepage.html",{'form':form,'task':task})
    

def delete(request,pk):
    task=Task.objects.get(id=pk)
    # task.delete()
    if request.method=="POST":
        task.delete()
        return redirect('/')
    return render(request,"todo/deletepage.html",{'task':task})