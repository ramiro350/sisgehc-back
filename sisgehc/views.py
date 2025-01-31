from rest_framework import viewsets
from sisgehc.models import Aluno, Curso, Evento, Professor, Inscricao, AtividadeComplementar, Coordenador
from sisgehc.serializer import AlunoSerializer, CursoSerializer, EventoSerializer, CoordenadorSerializer, ProfessorSerializer, InscricaoSerializer, ACSerializer

class AlunosViewSet(viewsets.ModelViewSet):
    """Exibindo todos os alunos e alunas"""
    queryset = Aluno.objects.all()
    serializer_class = AlunoSerializer

class CursosViewSet(viewsets.ModelViewSet):
    """Exibindo todos os cursos"""
    queryset = Curso.objects.all()
    serializer_class = CursoSerializer

class EventoViewSet(viewsets.ModelViewSet):
    """Exibindo todos os eventos"""
    queryset = Evento.objects.all()
    serializer_class = EventoSerializer

class ProfessorViewSet(viewsets.ModelViewSet):
    """Exibindo todos os professores"""
    queryset = Professor.objects.all()
    serializer_class = ProfessorSerializer

class InscricaoViewSet(viewsets.ModelViewSet):
    """Exibindo todas as inscrições"""
    queryset = Inscricao.objects.all()
    serializer_class = InscricaoSerializer

class CoordenadorViewSet(viewsets.ModelViewSet):
    """Exibindo todas as atividades complementares"""
    queryset = Coordenador.objects.all()
    serializer_class = CoordenadorSerializer

class AtividadeComplementarViewSet(viewsets.ModelViewSet):
    """Exibindo todas as atividades complementares"""
    queryset = AtividadeComplementar.objects.all()
    serializer_class = ACSerializer
