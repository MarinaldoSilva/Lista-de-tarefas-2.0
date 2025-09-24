from django.urls import path
from .views import TarefaListCreateAPIView, TarefaDetailAPIView


urlpatterns = [
    path('tarefas/', TarefaListCreateAPIView.as_view(), name='tarefasListCreate'),
    path('tarefas/<int:pk>/', TarefaDetailAPIView.as_view(), name='tarefasDetail')
]