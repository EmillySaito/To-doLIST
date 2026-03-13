from django.urls import path
from . import views

urlpatterns = [

    path("", views.login_view, name="login"),
    path("todo/", views.todo_view, name="todo"),
    path("concluir/<int:id>/", views.concluir_task, name="concluir"),
    path("editar/<int:id>/", views.editar_task, name="editar"),
    path("deletar/<int:id>/", views.deletar_task, name="deletar"),

]