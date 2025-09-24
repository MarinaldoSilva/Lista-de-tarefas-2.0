from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .services import TarefaService


class TarefaListCreateAPIView(APIView):

    def get(self, request):
        tarefa, error = TarefaService.get_tarefas()
        if error:
            return Response(error, status=status.HTTP_400_BAD_REQUEST)
        return Response(tarefa, status=status.HTTP_200_OK)
    
    def post(self, request):
        tarefa, error = TarefaService.create_tarefa(request.data)
        if error:
            return Response(error, status=status.HTTP_400_BAD_REQUEST)
        return Response(tarefa, status=status.HTTP_201_CREATED)
    
class TarefaDetailAPIView(APIView):

    def get(self, request, pk):
        tarefa, error = TarefaService.get_pk_tarefa(pk)
        if error:
            return Response(error, status=status.HTTP_400_BAD_REQUEST)
        return Response(tarefa, status=status.HTTP_200_OK)
    
    def put(self, request, pk):
        tarefa, error = TarefaService.update_tarefa(pk, request.data)
        if error:
            return Response(error, status=status.HTTP_400_BAD_REQUEST)
        return Response(tarefa, status=status.HTTP_200_OK)
    
    def patch(self, request, pk):
        tarefa, error = TarefaService.update_tarefa(pk, request.data)
        if error:
            return Response(error, status=status.HTTP_400_BAD_REQUEST)
        return Response(tarefa, status=status.HTTP_200_OK)
    
    def delete(self, request, pk):
        tarefa, error = TarefaService.delete_tarefa(pk)
        if error:
            return Response(error, status=status.HTTP_404_NOT_FOUND)
        return Response(status=status.HTTP_204_NO_CONTENT)