from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from .services import TarefaService
from .utils import get_status_error

class TarefaListCreateAPIView(APIView):

    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        tarefa, error = TarefaService.get_tarefas_by_user(request.user)
        if error:
            error_status = get_status_error(error)
            return Response(error, status=error_status)
        return Response(tarefa, status=status.HTTP_200_OK)
    
    def post(self, request):
        tarefa, error = TarefaService.create_tarefa(request.data, request.user)
        if error:
            error_status = get_status_error(error)
            return Response(error, status=error_status)
        return Response(tarefa, status=status.HTTP_201_CREATED)
    
class TarefaDetailAPIView(APIView):

    def get(self, request, pk):
        tarefa, error = TarefaService.get_pk_tarefa_by_user(pk, request.user)
        if error:
            error_status = get_status_error(error)
            return Response(error, status=error_status)
        return Response(tarefa, status=status.HTTP_200_OK)
    
    def put(self, request, pk):
        tarefa, error = TarefaService.update_tarefa_by_user(pk, request.data, request.user)
        if error:
            error_status = get_status_error(error)
            return Response(error, status=error_status)
        return Response(tarefa, status=status.HTTP_200_OK)
    
    def patch(self, request, pk):
        tarefa, error = TarefaService.update_tarefa_by_user(pk, request.data, request.user)
        if error:
            error_status = get_status_error(error)
            return Response(error, status=error_status)
        return Response(tarefa, status=status.HTTP_200_OK)
    
    def delete(self, request, pk):
        tarefa, error = TarefaService.delete_tarefa(pk, request.user)
        if error:
            error_status = get_status_error(error)
            return Response(error, status=error_status)
        return Response(status=status.HTTP_204_NO_CONTENT)