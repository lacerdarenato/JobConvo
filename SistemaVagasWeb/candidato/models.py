from django.db import models

ESCOLARIDADE_OPCOES = (
    ('1', 'Ensino Fundamental'),
    ('2', 'Ensino Medio'),
    ('3', 'Tecnólogo'),
    ('4', 'Ensino Superior'),
    ('5', 'Pós / MBA / Mestrado'),
    ('6', 'Doutorado'),
)

class candidato(models.Model):
    name = models.CharField(max_length=100)
    pretencaoSalarial = models.IntegerField()
    experiencia = models.CharField( max_length=100)
    escolaridade = models.CharField(max_length=1, choices=ESCOLARIDADE_OPCOES)

    def __str__(self):
        return self.name
