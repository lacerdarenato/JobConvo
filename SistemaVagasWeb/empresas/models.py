from django.db import models


class empresa(models.Model):

    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title
