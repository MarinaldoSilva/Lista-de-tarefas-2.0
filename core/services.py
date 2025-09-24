from .models import Tarefa
from .serializers import TarefaSerializer


class TarefaService:
    
    @staticmethod
    def get_tarefas():
        tarefas = Tarefa.objects.all()
        serializer = TarefaSerializer(tarefas, many=True)
        return serializer.data, None

    @staticmethod
    def create_tarefa(data):
        serializer = TarefaSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return serializer.data, None
        return None, serializer.errors
        
    @staticmethod
    def get_pk_tarefa(pk):
        try:
            tarefa = Tarefa.objects.get(pk=pk)
            serializer = TarefaSerializer(tarefa)
            return serializer.data, None
        except Tarefa.DoesNotExist:
            return None, {"errors":"Tarefa não localizada"}
    
    def update_tarefa(pk, data, partial=False):
        try:
            tarefa = Tarefa.objects.get(pk=pk)
        except Tarefa.DoesNotExist:
            return None, {"errors":"Tarefa não localizada"}
        
        serializer = TarefaSerializer(instance=tarefa, data=data, partial=partial)
        if serializer.is_valid():
            serializer.save()
            return serializer.data, None
        return None, serializer.errors
            
    @staticmethod
    def delete_tarefa(pk):
        try:
            tarefa = Tarefa.objects.get(pk=pk)
            tarefa.delete()
            return True, None
        except Tarefa.DoesNotExist:
            return False, {"errors":"Tarefa não localizada"}
        
        

        
        
        
    
