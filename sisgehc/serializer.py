from django.contrib.auth.models import User
from rest_framework import serializers
from sisgehc.models import Aluno, Curso, Evento, Professor, Inscricao, Coordenador, Presenca, AtividadeComplementar

class AlunoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Aluno
        fields = ['id_matricula', 'nome', 'horas_complementares', 'curso', 'senha']

    def create(self, validated_data):
        senha = validated_data.pop('senha')  # Extract senha field
        user = User.objects.create_user(username=validated_data['nome'], email='', password=senha)
        aluno = Aluno.objects.create(id_user=user, senha=senha,**validated_data)
        return aluno

class ProfessorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Professor
        fields = ['id_matricula', 'nome', 'senha', 'curso']

    def create(self, validated_data):
        senha = validated_data.pop('senha')
        user = User.objects.create_user(username=validated_data['nome'], email='', password=senha)
        professor = Professor.objects.create(id_user=user, **validated_data)
        return professor

class CoordenadorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Coordenador
        fields = ['id_matricula', 'nome', 'senha', 'curso']

    def create(self, validated_data):
        senha = validated_data.pop('senha')
        user = User.objects.create_user(username=validated_data['nome'], email='', password=senha)
        coordenador = Coordenador.objects.create(id_user=user, **validated_data)
        return coordenador

class CursoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Curso
        fields = '__all__'

class EventoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Evento
        fields = '__all__'

class InscricaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Inscricao
        fields = ['id_inscricao', 'evento', 'aluno']

class PresencaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Presenca
        fields = ['id_presenca', 'inscricao']

class ACSerializer(serializers.ModelSerializer):
    class Meta:
        model = AtividadeComplementar
        fields = '__all__'

class LoginSerializer(serializers.Serializer):
    """Serializer to validate login request data"""
    username = serializers.CharField(required=True)
    password = serializers.CharField(write_only=True, required=True)