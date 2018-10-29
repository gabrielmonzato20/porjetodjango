from django.db import models
from  .aluno import *

class Professor(models.Model):
    def __str__(self):
        return self.nome + self.email
    def save(self):
    	if self.login == "":
    		raise Exception('')
    	if self.email == "":
    		self.email = 'email nao fornecido'
    	if len(Professor.objects.filter(login=self.login))!=0:
    		raise Exception("")
        if len(Professor.objects.filter(login=self.login))!=0 and Aluno.objects.filter(login=self.login)!=0:
    		raise Exception("")
    	super(Professor,self).save()
    nome = models.TextField(max_length=255)
    email = models.TextField(max_length=255)
    celular = models.TextField(max_length=20)
    login = models.TextField(max_length=20)
    senha = models.TextField(max_length=20)