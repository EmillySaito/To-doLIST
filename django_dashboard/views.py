from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from .models import Task


def login_view(request):

    if request.method == "POST":

        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)

        if user:
            login(request, user)
            return redirect("todo")

    return render(request, "django_dashboard/login.html")


@login_required
def todo_view(request):

    if request.method == "POST":

        nome = request.POST.get("nome")
        tipo = request.POST.get("tipo")
        data = request.POST.get("data")

        if not nome or not tipo or not data:

            tarefas_afazer = Task.objects.filter(user=request.user, concluida=False)
            tarefas_feitas = Task.objects.filter(user=request.user, concluida=True)

            return render(request, "django_dashboard/todo.html", {
                "erro": "Preencha todos os campos!",
                "afazer": tarefas_afazer,
                "feitas": tarefas_feitas
            })

        Task.objects.create(
            user=request.user,
            nome=nome,
            tipo=tipo,
            data_conclusao=data
        )

        return redirect("todo")

    tarefas_afazer = Task.objects.filter(user=request.user, concluida=False)
    tarefas_feitas = Task.objects.filter(user=request.user, concluida=True)

    return render(request, "django_dashboard/todo.html", {
        "afazer": tarefas_afazer,
        "feitas": tarefas_feitas
    })
@login_required
def concluir_task(request, id):

    tarefa = get_object_or_404(Task, id=id, user=request.user)

    tarefa.concluida = True
    tarefa.save()

    return redirect("todo")


@login_required
def editar_task(request, id):

    tarefa = get_object_or_404(Task, id=id, user=request.user)

    if request.method == "POST":

        tarefa.nome = request.POST.get("nome")
        tarefa.tipo = request.POST.get("tipo")
        tarefa.data_conclusao = request.POST.get("data")

        tarefa.save()

        return redirect("todo")

    return render(request, "django_dashboard/editar.html", {"tarefa": tarefa})


@login_required
def deletar_task(request, id):

    tarefa = get_object_or_404(Task, id=id, user=request.user)

    tarefa.delete()

    return redirect("todo")