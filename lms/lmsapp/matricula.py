from django.db import models
from .disciplinaofertada import *


class Matricula(models.Model):
    def save(self):
        if len(Matricula.objects.all())>=3:
            raise Exception("")

        disciplina_matricula = self.ofertada_para_disciplina(self.disciplinaOfertada)
        disciplinas_aluno = []
        matriculas_aluno = Matricula.objects.filter(aluno=self.aluno)
        for matricula in matriculas_aluno:
            disciplinas_aluno.append(self.ofertada_para_disciplina(matricula.disiplinaOfertada))

        if disciplina_matricula in disciplinas_aluno:
            raise Exception('')

        #if len(DisciplinaOfertada.objects.filter(disciplina = self.disciplina_para_ofertada(disciplinaOfertada) )) >1:
        #    raise Exception('')
            
        super().save()
    aluno = models.IntegerField(null=True) 
    disiplinaOfertada=models.IntegerField(null=True)
    
           

    def ofertada_para_disciplina(self,disciplinaOfertadaId):
        disciplinasOfertadas = DisciplinaOfertada.objects.filter(id=disciplinaOfertadaId)
        disciplinaOfertada = disciplinasOfertadas[0]
        nro_disciplina = disciplinaOfertada.disciplina
        return nro_disciplina 
    '''erro null    aluno = models.IntegerField() 
    disiplinaOfertada=models.IntegerField() '''
''' if Matricula.objects.filter(aluno=self.aluno)) len(DisciplinaOfertada.objects.filter(id=self.disiplinaOfertada)[0].disciplina):'''

