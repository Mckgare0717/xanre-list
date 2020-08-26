from django.shortcuts import render,redirect
from django.http import HttpResponse
from todolist.models import tasklist
from todolist.forms import taskform
from django.contrib import messages
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
# Create your views here.



@login_required
def todolist_app(request):
    if request.method == "POST":
        form = taskform(request.POST or None)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.manage = request.user
            instance.save()
            
        messages.success(request , ("new task added!!"))
        return redirect('/task')
    else:
        all_task = tasklist.objects.filter(manage = request.user)
        paginator = Paginator(all_task, 5)
        page = request.GET.get('pg')
        all_task = paginator.get_page(page,)
        return render(request, 'todolist.html', {'all_task': all_task})

@login_required
def delete_task(request, task_id):
    task = tasklist.objects.get(pk=task_id)
    if task.manage == request.user:
        task.delete()
    else:
        messages.error(request , ("access restricted , access not allowed"))
    return redirect('/task')

@login_required
def edit_task(request,task_id):
    if request.method == "POST":
        task = tasklist.objects.get(pk=task_id)
        form = taskform(request.POST or None, instance=task)
        print(task)
        if form.is_valid():
            form.save()
        return redirect('/task')
    else:
        task_obj = tasklist.objects.get(pk=task_id)
        return render(request, 'edit.html', {'task_obj': task_obj})

@login_required
def complete_task(request,task_id):
    task = tasklist.objects.get(pk=task_id)
    if task.manage == request.user:
        task.done = True
        task.save()
    else:
         messages.error(request , ("access restricted , access not allowed"))
    return redirect('/task')


@login_required
def pending_task(request,task_id):
    task = tasklist.objects.get(pk=task_id)
    if task.manage == request.user:
        task.done = False
        task.save()
    else:
        messages.error(request , ("access restricted , access not allowed"))
    return redirect('/task')

def index(request):
    context = {
        'index_text' :'welcome to welcome to index page' 
        }
    return render(request, 'index.html', context)



def contact(request):
    context = {
        'contact_text' :'welcome to contact page' 
        }
    return render(request, 'contact.html', context)



def about(request):
    context = {
        'about_text' :'welcome to welcome to about page' 
        }
    return render(request, 'about.html', context)