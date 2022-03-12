from django.http import HttpResponseRedirect
from django.shortcuts import render

from .models import TodoListItem
# Create your views here.

def todoView(request):
    all_todos = TodoListItem.objects.all()
    return render(request, 'todolist.html', {"all_items" : all_todos})

def addToDo(request):
    x = request.POST["content"]
    new_item = TodoListItem(content = x)
    new_item.save()
    return HttpResponseRedirect("/todos/")

def deleteToDo(request, i):
    x = TodoListItem.objects.get(id = i)
    x.delete()
    return HttpResponseRedirect('/todos/')

