from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import RetrieveAPIView
from rest_framework.parsers import MultiPartParser, FormParser
from sisgehc.models import Aluno, Curso, Evento, Professor, Inscricao, AtividadeComplementar, Coordenador
from sisgehc.serializer import AlunoSerializer, CursoSerializer, EventoSerializer, CoordenadorSerializer, ProfessorSerializer, InscricaoSerializer, ACSerializer
from sisgehc.serializer import LoginSerializer
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from rest_framework.permissions import IsAuthenticated

class AlunosViewSet(viewsets.ModelViewSet):
    """Exibindo todos os alunos e alunas"""
    queryset = Aluno.objects.all()
    serializer_class = AlunoSerializer
    permission_classes = [IsAuthenticated]

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

class SubmeterAtividadeViewSet(viewsets.ModelViewSet):
    """submetendo as atividads externas"""
    queryset =  AtividadeComplementar.objects.all()
    serializer_class = ACSerializer

    def create(self, request, *args, **kwargs):
        arquivo = request.FILES.get('arquivo_certificado')  # Salva o arquivo temporariamente
        data = request.data.dict()  # Copia os dados, ignorando arquivos
        if arquivo:
            data['arquivo_certificado'] = arquivo  # Reinsere o arquivo

        serializer = self.get_serializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class LoginView(APIView):
    """Handles login for Aluno, Professor, and Coordenador"""
    
    def post(self, request):
        serializer = LoginSerializer(data=request.data)  # Validate request data
        if serializer.is_valid():
            username = serializer.validated_data["username"]
            password = serializer.validated_data["password"]

            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
            
            # Determine user type
            # user_type = None
            # if Aluno.objects.filter(id_user=user).exists():
            #     user_type = "Aluno"
            # elif Professor.objects.filter(id_user=user).exists():
            #     user_type = "Professor"
            # elif Coordenador.objects.filter(id_user=user).exists():
            #     user_type = "Coordenador"

                return Response({
                    "message": "Login successful"
                    # "user_type": user_type
                }, status=status.HTTP_200_OK)
        
            return Response({"error": "Invalid credentials"}, status=status.HTTP_401_UNAUTHORIZED)

class LogoutView(APIView):
    """Handles user logout"""
    permission_classes = [IsAuthenticated]  # 👈 Requires login

    def post(self, request):
        logout(request)  # Logs out the user
        return Response({"message": "Logout successful"}, status=status.HTTP_200_OK)