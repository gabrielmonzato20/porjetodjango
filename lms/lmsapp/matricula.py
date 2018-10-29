from django.db import models
from .disciplinaofertada import *


class Matricula(models.Model):
    def save(self):
        if len(Matricula.objects.all())>=3:
            raise Exception("")    
        super().save()
    aluno = models.IntegerField(null=True) 
    disiplinaOfertada=models.IntegerField(null=True)

    def disciplina_para_ofertada(self,disciplinaOfertada):
        disciplinasOfertadas = DisciplinaOfertada.objects.filter(id=disciplinaOfertada)
        disciplinaOfertada = disciplinas[0]
        nro_disciplina = disciplinaOfertada.disciplina
        return nro_disciplina 
    '''erro null    aluno = models.IntegerField() 
    disiplinaOfertada=models.IntegerField() '''
''' if Matricula.objects.filter(aluno=self.aluno)) len(DisciplinaOfertada.objects.filter(id=self.disiplinaOfertada)[0].disciplina):'''

