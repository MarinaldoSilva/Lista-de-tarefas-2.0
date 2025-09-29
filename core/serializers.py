from rest_framework import serializers
from .models import Tarefa


class TarefaSerializer(serializers.ModelSerializer):
      
    """
    essa informação vem do banco(serializar objs python p/ json), não vem do cliente, retorna para o cliente a informação do dono.username, ou seja, o nome do criador da nota, após comparação do token que vem no header no campo Authorization, a consulta no banco é feito e se for um user valido, vai buscar o nome do dono que detem deteminado token
    """
    dono = serializers.ReadOnlyField(source = 'dono.username')

    class Meta:
        model = Tarefa
        fields = ['id', 'dono','descricao', 'concluido', 'data_criacao', 'prioridade']
        read_only_fields = ['id', 'data_criacao', 'dono']

   
