from django.urls import path
from .views import CreateTask, DoneTaskView, DeleteTodo, EditTaskView

urlpatterns = [
    path("", CreateTask.as_view(), name="todo"),
    path("done_todo", DoneTaskView.as_view(), name="done_todo"),
    path('delete/<int:task_id>', DeleteTodo.as_view(), name="delete"),
    path('edit/<int:task_id>', EditTaskView.as_view(), name="edit")
]
