from django.db import models

class tb_users(models.Model):
	name=models.CharField(max_length=50)
	email=models.EmailField()
	passw=models.CharField(max_length=50)
	number=models.CharField(max_length=50)
	def __str__(self):
		return f'{self.name},{self.email},{self.passw},{self.number}'

class tb_notas(models.Model):
	title=models.CharField(max_length=50)
	subtitle=models.EmailField(max_length=50)
	text=models.CharField(max_length=50)
	cor=models.CharField(max_length=120)
	def __str__(self):
		return f'{self.title},{self.subtitle},{self.text},{self.cor}'

class tb_categorias(models.Model):
	catename=models.CharField(max_length=50)
	def __str__(self):
		return f'{self.catename}'
