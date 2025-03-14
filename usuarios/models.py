from django.db import models

class Servico(models.Model):
    nome = models.CharField(max_length=100) 
    data = models.DateField() 
    valor = models.DecimalField(max_digits=10, decimal_places=2) 
    descricao = models.TextField()

    def __str__(self):
        return self.nome