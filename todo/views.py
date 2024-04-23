from django.shortcuts import render, redirect
from django.urls import reverse
from django.http.response import HttpResponse
from django.views import View
from .forms import TodoForms
from .models import Todo


class CreateTask(View):
    template_name = "index.html"

    def get(self, request):
        todos = Todo.objects.filter(completed = False)
        dones = Todo.objects.filter(completed = True)
        context = {
            'todos': todos,
            'done_todos': dones,
            'dones': dones.count(),
            'total': todos.count() + dones.count()
        }
        return render(request, self.template_name, context)
    
    def post(self, request):
        print('am here now')
        print(request.POST)
        if request.POST:
            todo_name = request.POST.get('todo')

            try:
                new_todo = Todo.objects.create(title=todo_name, completed = False)
                new_todo.save()
            except Exception as e:
                return "An Error Occured"
            
        return redirect(reverse('todo'))
    
class DoneTaskView(View):
    template_name = "index.html"

    def get(self, request):
        todos = Todo.objects.filter(completed = False)
        dones = Todo.objects.filter(completed = True)
        context = {
            'todos': todos,
            'done_todos': dones,
            'dones': dones.count(),
            'total': todos.count() + dones.count()
        }
        return render(request, self.template_name, context)
    
    def post(self, request):
        if request.POST:
            dones = request.POST.getlist('dones[]')

            if dones is not None:
                print(dones)
                for done_id in dones:
                    #get the task using the id
                    todo = Todo.objects.get(id=done_id)

                    #change the status of completed 
                    todo.completed = True

                    #Save
                    todo.save()
           

        return redirect('todo')
    
class EditTaskView(View):
    template_name = 'edit.html'

    def get(self, request, task_id):
        task = Todo.objects.get(id=task_id)

        context = {
            'task': task,
        }

        return render(request, self.template_name, context)
    
    def post(self, request, task_id):
        title = request.POST.get('title')

        print(request.POST)
        task = Todo.objects.get(id=task_id)

        task.title = title
        task.save()

        return redirect('todo')

    
        
class DeleteTodo(View):
    template_name = "delete.html"

    def get(self, request, task_id):
        task = Todo.objects.get(id=task_id)

        context = {
            'task': task,
        }

        return render(request, self.template_name, context)

    def post(self, request, task_id):
        #get the task
        todo = Todo.objects.get(id=task_id)
        print(todo)
        #delete the task
        todo.delete()

        #redirect to the index.html
        return redirect(reverse('todo'))