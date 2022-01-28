from django.db import models

class UsuarioModel(models.Model):
	nome = models.CharField(max_length = 200)
	cpf = models.CharField(max_length = 11)
	datanascimento = models.DateField()

	def __str__(self):
		return self.nome


