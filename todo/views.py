from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.views.generic import ListView,View
from django.views.generic.edit import CreateView ,UpdateView
# Create your views here.
from .models import Todo


class HomePageView(ListView):
    model = Todo
    template_name = "index.html"
    ordering = "-id"


    
class DoneToDo(View):

    def get(self,request,todo_id):
        todo = Todo.objects.get(id=todo_id)
        todo.doned = True
        todo.save()
        return redirect("/")


def add_todo(request):
    todo_title = request.GET.get("todo")
    priority = request.GET.get("priority")
    Todo.objects.create(title=todo_title, priority=priority)
    return redirect("/")

def delete(request, todo_id):
    todo = Todo.objects.get(id=todo_id)
    todo.delete()
    return redirect("/")