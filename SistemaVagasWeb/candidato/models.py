from django.db import models
from django.contrib.auth import get_user_model

ESCOLARIDADE_OPCOES = (
    ('1', 'Ensino Fundamental'),
    ('2', 'Ensino Medio'),
    ('3', 'Tecnólogo'),
    ('4', 'Ensino Superior'),
    ('5', 'Pós / MBA / Mestrado'),
    ('6', 'Doutorado'),
)


class candidato(models.Model):
    nome = models.CharField(max_length=100)
    pretencaoSalarial = models.IntegerField()
    experiencia = models.CharField(max_length=100)
    escolaridade = models.CharField(max_length=1, choices=ESCOLARIDADE_OPCOES)
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)

    def __str__(self):
        return self.nome
