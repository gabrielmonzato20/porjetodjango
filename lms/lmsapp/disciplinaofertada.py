from django.db import models
from lmsapp.aluno import *
from lmsapp.disciplina import *
class DisciplinaOfertada(models.Model):
	def __str__(self):
		return self.curso 
	def save(self):
		if self.curso not in ['ADS', 'SI','BD']:
			raise Exception('')
		if len(DisciplinaOfertada.objects.filter(ano=self.ano ,semestre=self.semestre, turma=self.turma, curso=self.curso , disciplina=self.disciplina)) >=1:
			raise Exception("")
		if len(Professor.objects.filter(id=self.professor))<1:
			raise Exception("")
		if len(Disciplina.objects.filter(id=self.disciplina))<1:
			raise Exception("")
		super(DisciplinaOfertada,self).save()
        


	curso = models.TextField(max_length=255)
	turma = models.TextField(max_length=5)
	ano = models.IntegerField() 
	semestre = models.IntegerField() 
	professor = models.IntegerField() 
	disciplina = models.IntegerField() 