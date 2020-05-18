from django.shortcuts import render
from django.http import HttpResponse , HttpResponseRedirect
import requests
from .models import TodoItem

# Create your views here.
def todoView(request):
    all_todo_items = TodoItem.objects.all()
    return render(request , 'todo_app.html' , 
    {'all_items':all_todo_items})

def addTodo(request):
    #create a new todo all_items
    #and save , then redirect to the earlier page
    #z = requests.post['content']
    new_item = TodoItem(content = request.POST['content'])
    new_item.save()

    return HttpResponseRedirect('/todo_app/')

def deleteTodo(request , todo_id):
    item_to_delete = TodoItem.objects.get(id = todo_id)
    item_to_delete.delete()

    return HttpResponseRedirect('/todo_app/')

