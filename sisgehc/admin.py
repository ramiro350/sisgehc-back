from django.contrib import admin
from sisgehc.models import Aluno, Curso, Professor, Coordenador, Evento, Inscricao, AtividadeComplementar

class Alunos(admin.ModelAdmin):
    list_display = ('id_matricula', 'nome', 'horas_complementares', 'curso')
    list_display_links = ('id_matricula', 'nome')
    search_fields = ('nome',)
    list_per_page = 20
admin.site.register(Aluno, Alunos)

class Cursos(admin.ModelAdmin):
    list_display = ('id_curso', 'nome')
    list_display_links = ('id_curso', 'nome')
    search_fields = ('nome',)
    list_per_page = 20
admin.site.register(Curso, Cursos)

class Professores(admin.ModelAdmin):
    list_display = ('id_matricula', 'nome', 'curso', 'senha')
    list_display_links = ('id_matricula', 'nome')
    search_fields = ('nome',)
    list_per_page = 20
admin.site.register(Professor, Professores)

class Coordenadores(admin.ModelAdmin):
    list_display = ('id_matricula', 'nome', 'curso', 'senha')
    list_display_links = ('id_matricula', 'nome')
    search_fields = ('nome',)
    list_per_page = 20
admin.site.register(Coordenador, Coordenadores)

class Eventos(admin.ModelAdmin):
    list_display = ('id_evento', 'nome', 'professor', 'curso', 'tipo', 'horas_complementares', 
                    'data_inicio', 'data_encerramento', 'hora_inicio', 'hora_encerrado', 'descricao_evento')
    list_display_links = ('id_evento', 'nome')
    search_fields = ('nome',)
    list_per_page = 20
admin.site.register(Evento, Eventos)

class Inscricoes(admin.ModelAdmin):
    list_display = ('id_inscricao', 'evento', 'aluno', 'participacao_boolean', 'porcent_participacao')
    list_display_links = ('id_inscricao',)
    search_fields = ('evento__nome', 'aluno__nome')
    list_per_page = 20
admin.site.register(Inscricao, Inscricoes)

class AtividadesComplementares(admin.ModelAdmin):
    list_display = ('id_atividade', 'aluno', 'carga_horaria', 'coordenador', 'data_submissao', 'tipo_atividade', 'area_de_conhecimento')
    list_display_links = ('id_atividade',)
    search_fields = ('aluno__nome', 'tipo_atividade')
    list_per_page = 20
admin.site.register(AtividadeComplementar, AtividadesComplementares)
