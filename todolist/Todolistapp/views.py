from django.shortcuts import render,redirect
from .models import Todo_data
# Create your views here.
def Todolist(request):
    todolist=Todo_data.objects.all()
    return render(request, 'index.html', {'todolist': todolist})
def add_task(request):
    if request.method == 'POST':
        task=request.POST.get('task')
        todo_data=Todo_data(
            task=task
        )
        todo_data.save()
        return redirect('Todolist')
    return render(request,'addtask',{'todolist': todo_data})
def edit_task(request,id):
    if request.method == 'POST':
        task=request.POST.get('task')
        todo_data=Todo_data(
            id=id,
            task=task
        )
        todo_data.save()
        return redirect('Todolist')
    return render(request,'edittask',{'todolist': todo_data})
def delete_task(request,id):
    task=Todo_data.objects.filter(id=id)
    task.delete()
    return redirect('Todolist')