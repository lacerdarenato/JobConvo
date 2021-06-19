from django.db import models
from django.contrib.auth import get_user_model
from candidato.models import candidato


class vaga (models.Model):

    SALARY = (
        ('1', 'ATÉ 1000,00'),
        ('2', 'DE 1000,01 ATÉ 2000,00'),
        ('3', 'DE 3000,01 ATÉ 3000,00'),
        ('4', 'ACIMA DE 3000,01')
    )
    EDUCATION_LEVEL = (
        ('1', 'Ensino Fundamental'),
        ('2', 'Ensino Medio'),
        ('3', 'Tecnólogo'),
        ('4', 'Ensino Superior'),
        ('5', 'Pós / MBA / Mestrado'),
        ('6', 'Doutorado'),
    )
    title = models.CharField(max_length=255)
    requirements = models.TextField()
    salaryRange = models.CharField(max_length=1, choices=SALARY)
    minimalEducationLevel = models.CharField(max_length=1, choices=EDUCATION_LEVEL)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    subscript = models.ManyToManyField(candidato, through='Candidatura')

    def __str__(self):
        return self.title


class Candidatura(models.Model):

    cand = models.ForeignKey(candidato, on_delete=models.CASCADE)
    vaga = models.ForeignKey(vaga, on_delete=models.CASCADE)
