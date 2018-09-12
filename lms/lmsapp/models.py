from django.db import models

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
    	super(Professor,self).save()

    nome = models.TextField(max_length=255)
    email = models.TextField(max_length=255)
    celular = models.TextField(max_length=20)
    login = models.TextField(max_length=20)
    senha = models.TextField(max_length=20)
class Disciplina(models.Model):
	def __str__(self):
		return self.ementa + " "+self.nome
	def save(self):
		if len(Disciplina.objects.filter(nome = self.nome)) >=1:
			raise Exception('')
		super(Disciplina,self).save()
	nome = models.TextField(max_length=50)
	ementa = models.TextField(max_length=5000)
class DisciplinaOfertada(models.Model):
	def __str__(self):
		return self.curso 
	def save(self):
		if self.curso not in ['ADS', 'SI','BD']:
			raise Exception('')
		if len(DisciplinaOfertada.objects.filter(ano=self.ano ,semestre=self.semestre, turma=self.turma, curso=self.curso , disciplina=self.disciplina)) >=1:
			raise Exception("")
		super(DisciplinaOfertada,self).save()
	curso = models.TextField(max_length=255)
	turma = models.TextField(max_length=5)
	ano = models.IntegerField() 
	semestre = models.IntegerField() 
	professor = models.IntegerField() 
	disciplina = models.IntegerField() 


