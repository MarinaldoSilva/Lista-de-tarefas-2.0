from .models import Tarefa
from .serializers import TarefaSerializer

msg_error = "ID não localizado ou usuário sem permissão para acesso."

class TarefaService:
    
    @staticmethod
    def get_tarefas_by_user(user):
        tarefas = Tarefa.objects.filter(dono=user)
        serializer = TarefaSerializer(tarefas, many=True)
        return serializer.data, None

    @staticmethod
    def create_tarefa(data, user):
        serializer = TarefaSerializer(data=data)
        if serializer.is_valid():
            serializer.save(dono=user)
            """
            no momento que a requisição é feita, o middleware do django vai no cabeçalho da requisição e procura o Authorization Token, pega o valor do token, vai no banco e verifica se é o mesmo da requisição, caso sejá, libera o acesso a view, que encaminha para o service e após o processo chegar no serializer.is_valid(), podemos adicionar o dono que vem no request.user no nosso .save(dono=user), e quando os dados forem salvos, o dono vai ser passado junto pois o obj já esta ok no banco, assim o meu token que já está vinculado ao meu ID, pega o meu username e carimba na minha tarefa.
            """
            return serializer.data, None
        return None, serializer.errors
        
    @staticmethod
    def get_pk_tarefa_by_user(pk, user):
        try:
            tarefa = Tarefa.objects.get(pk=pk, dono=user)
            serializer = TarefaSerializer(tarefa)
            return serializer.data, None
        except Tarefa.DoesNotExist:
            return None, {"Errors": msg_error}
    
    @staticmethod
    def update_tarefa_by_user(data, pk, user, partial=False):
        try:
            tarefa = Tarefa.objects.get(pk=pk, dono=user)
        except Tarefa.DoesNotExist:
            return None, {"Errors": msg_error}
        
        serializer = TarefaSerializer(instance=tarefa, data=data, partial=partial)
        if serializer.is_valid():
            serializer.save()
            return serializer.data, None
        return None, serializer.errors
            
    @staticmethod
    def delete_tarefa(pk, user):
        try:
            tarefa = Tarefa.objects.get(pk=pk, dono=user)
            tarefa.delete()
            return True, None
        except Tarefa.DoesNotExist:
            return False, {"Errors": msg_error}
        
        

        
        
        
    
