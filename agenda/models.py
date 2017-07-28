
from __future__ import unicode_literals
from django.db  import models

#
# ItemAgenda
#
class ItemAgenda(models.Model):
    data = models.DateField()
    hora = models.TimeField()
    titulo = models.CharField(max_length=100)
    descricao = models.TextField(blank=True)


