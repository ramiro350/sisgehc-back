from django.db import models


class Curso(models.Model):
    id_curso = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome


class Aluno(models.Model):
    id_matricula = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=100)
    senha = models.CharField(max_length=50)
    horas_complementares = models.IntegerField(default=0)
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome


class Professor(models.Model):
    id_matricula = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=100)
    senha = models.CharField(max_length=50)
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome


class Coordenador(models.Model):
    id_matricula = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=100)
    senha = models.CharField(max_length=50)
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome


class Evento(models.Model):
    id_evento = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=200)
    professor = models.ForeignKey(Professor, on_delete=models.CASCADE)
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    tipo = models.CharField(max_length=50)
    horas_complementares = models.IntegerField()
    data_inicio = models.DateField()
    data_encerramento = models.DateField()
    hora_inicio = models.TimeField()
    hora_encerrado = models.TimeField()
    limite_inscricao = models.DateField()
    descricao_evento = models.TextField()

    def __str__(self):
        return self.nome


class Inscricao(models.Model):
    id_inscricao = models.AutoField(primary_key=True)
    evento = models.ForeignKey(Evento, on_delete=models.CASCADE)
    aluno = models.ForeignKey(Aluno, on_delete=models.CASCADE)
    participacao_boolean = models.BooleanField(default=False)
    porcent_participacao = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return f"Inscrição {self.id_inscricao} - Evento: {self.evento.nome}"


class Presenca(models.Model):
    id_presenca = models.AutoField(primary_key=True)
    inscricao = models.ForeignKey(Inscricao, on_delete=models.CASCADE)

    def __str__(self):
        return f"Presença {self.id_presenca}"


class AtividadeComplementar(models.Model):
    id_atividade = models.AutoField(primary_key=True)
    aluno = models.ForeignKey(Aluno, on_delete=models.CASCADE)
    carga_horaria = models.IntegerField()
    coordenador = models.ForeignKey(Coordenador, on_delete=models.CASCADE)
    data_submissao = models.DateField()
    data_validacao = models.DateField(null=True, blank=True)
    arquivo_certificacao = models.FileField(upload_to="certificados/")
    tipo_atividade = models.CharField(max_length=100)
    sub_tipo = models.CharField(max_length=100, null=True, blank=True)
    area_de_conhecimento = models.CharField(max_length=100)

    def __str__(self):
        return f"Atividade {self.id_atividade} - {self.tipo_atividade}"
