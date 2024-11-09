from django.urls import path 
from . import views

app_name = "todo"

urlpatterns = [
    path("", views.HomePageView.as_view(), name="home"),
    
    path("add/todo", views.add_todo, name="add_todo"),
    path('done/<int:todo_id>', views.DoneToDo.as_view(),name='done'),
    path('delete/<int:todo_id>', views.delete,name='delete'),
    
]
