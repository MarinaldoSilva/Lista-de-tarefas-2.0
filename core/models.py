from django.db import models

class Tarefa(models.Model):

    """criar os choices em uma classe seprada dentro de Tarefa"""
    class Prioridade(models.IntegerChoices):
        BAIXA = 1, 'Baixa'
        MEDIA = 2, 'Média'
        ALTA = 3, 'Alta'
    """
        A classe Prioridade cria automaticamente, a propriedade chamada 'choices', essa propriedade cria a lista de tuplas [(1, 'Baixa'), (2, 'Média'), (3, 'Alta')] que o IntegerField precisa.
    """

    descricao = models.TextField()
    concluido = models.BooleanField(default=False)
    data_criacao = models.DateTimeField(auto_now_add=True)
    """
    estamos dizendo que os valores que serão salvos no banco de dados são números inteiros(models.IntegerChoices)"""
    prioridade = models.IntegerField(
        choices = Prioridade.choices,
        default = Prioridade.MEDIA
    )

    def __str__(self):
        return self.descricao