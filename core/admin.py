from django.contrib import admin
from .models import Tarefa

@admin.register(Tarefa)
class AdminTarefa(admin.ModelAdmin):
    list_display = ['dono','descricao','concluido', 'data_criacao', 'prioridade']
    search_fields = ['descricao','dono__username']
