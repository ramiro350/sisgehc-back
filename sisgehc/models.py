from django.db import models


class Curso(models.Model):
    nome = models.CharField(max_length=50)

    def __str__(self):
        return self.nome

class Aluno(models.Model):
    nome = models.CharField(max_length=50)
    matricula = models.IntegerField()
    senha = models.CharField(max_length=30)
    horasComplementares = models.IntegerField()
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome

class Professor(models.Model):
    nome = models.CharField(max_length=50)
    matricula = models.IntegerField()
    senha = models.CharField(max_length=30)
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    def __str__(self):
        return self.nome


class Evento (models.Model):
    nome = models.CharField(max_length=50)
    horasComplementares = models.IntegerField()
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    professor = models.CharField(max_length=50 , blank=True, null=True)
    responsavel = models.CharField(max_length=50, null=True, blank=True)
    dataInicio = models.DateField()
    dataFim = models.DateField()
    horaInicio = models.TimeField() 
    horaFim = models.TimeField()      
    descricao = models.CharField(max_length=200)
    imagem = models.ImageField(upload_to='fotos/', null=True, blank=True)
    def __str__(self):
        return self.nome


class Inscricao (models.Model):
    evento = models.ForeignKey(Evento, on_delete=models.CASCADE)
    Aluno = models.ForeignKey(Aluno, on_delete=models.CASCADE)

class Attendance (models.Model):
    inscricao = models.ForeignKey(Inscricao, on_delete=models.CASCADE)
    status = (
        ('P', 'Presente'),
        ('F', 'Falta')
       
    )
    

