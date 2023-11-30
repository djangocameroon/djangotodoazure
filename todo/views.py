from django.shortcuts import render
from django.http.response import HttpResponse
from .forms import TodoForms
from .models import Todo


def todolist(request):
    todo = Todo.objects.all()
    form = TodoForms()
    if request.method == 'POST':
        form = TodoForms(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("Hurray!!! Success")
    context = {
        'form': form,
        'todo': todo
    }
    return render(request, "index.html", context)
