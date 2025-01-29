from rest_framework import serializers
from sisgehc.models import Aluno, Curso, Evento, Professor, Inscricao, CoordenadorModel, Presenca, AtividadeComplementar

class AlunoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Aluno
        fields = ['id_matricula', 'nome', 'horasComplementares', 'curso','senha']

class CursoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Curso
        fields = '__all__'

class EventoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Evento
        fields = '__all__'
        

class ProfessorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Professor
        fields = ['id_matricula','nome','senha', 'curso']


class InscricaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Inscricao
        fields = ['id_inscricao','evento', 'aluno']

class CoordenadorSerializer(serializers.ModelSerializer):
    class Meta:
        model = CoordenadorModel
        fields = ['id_matricula', 'nome', 'senha', 'curso']

class PresencaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Presenca
        fields = ['id_presenca','inscricao']

class ACSerializer(serializers.ModelSerializer):
    class Meta:
        model = AtividadeComplementar
        fields = ['id_atividade',
                  'aluno',
                  'carga_horaria',
                  'coordenador',
                  'data_submissao',
                  'data_validacao'
                  ]
