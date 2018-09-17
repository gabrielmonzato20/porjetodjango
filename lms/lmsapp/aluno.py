from django.db import models
from lmsapp.professor import *
class Aluno(models.Model):
    def save(self):
     	if self.email == "":
     		self.email =  'email nao fornecido'
     	if self.login=='':
     		raise Exception('')
     	if len(Aluno.objects.filter(login=self.login))>0:
     		raise Exception('')
     	if len(Professor.objects.filter(login=self.login)) == len(Aluno.objects.filter(login=self.login)) and len(Aluno.objects.filter(login=self.login)) > 1 or len(Professor.objects.filter(login=self.login)):
     		raise Exception("")
     	super(Aluno,self).save()
    nome = models.TextField(max_length=255)
    email =models.TextField(max_length=255)
    celular = models.TextField(max_length=20)
    login = models.TextField(max_length=20)
    senha = models.TextField(max_length=20)