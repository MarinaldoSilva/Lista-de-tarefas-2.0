from rest_framework import serializers
from .models import Tarefa


class TarefaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tarefa
        fields = ['id', 'descricao', 'concluido', 'data_criacao', 'prioridade']
        read_only_fields = ['id', 'data_criacao']

   
