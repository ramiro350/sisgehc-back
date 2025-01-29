from django.contrib import admin

from sisgehc.models import Aluno, Curso, Professor, Evento, Inscricao, CoordenadorModel

class Alunos(admin.ModelAdmin):
    list_display = ('id_matricula','nome','senha', 'horas_complementares', 'curso')
    list_display_links = ('id_matricula', 'nome')
    search_fields = ('nome',)
    list_per_page = 20
admin.site.register(Aluno, Alunos)

class Cursos (admin.ModelAdmin):
    list_display = ('id_curso','nome')
    list_display_links = ('id_curso', 'nome')
    search_fields = ('nome',)
    list_per_page = 20
admin.site.register(Curso, Cursos)

class Professores(admin.ModelAdmin):
    list_display = ('id_matricula','nome', 'curso', 'senha')
    list_display_links = ('id_matricula', 'nome')
    search_fields = ('nome',)
    list_per_page = 20
admin.site.register(Professor, Professores)

class Coordenador(admin.ModelAdmin):
    list_display = ('id_matricula','nome', 'curso','senha')
    list_display_links = ('id_matricula','nome')
    seach_fields = ('nome',)
admin.site.register(CoordenadorModel, Coordenador)

class Eventos (admin.ModelAdmin):
    list_display = ('id_evento','nome', 'professor', 'curso', 'tipo','horas_complementares', 'data_inicio', 'data_encerramento', 'hora_inicio', 'hora_encerrado', 'limite_inscricao','descricao_evento')
    list_display_links = ('id_evento', 'nome')
    search_fields = ('nome',)
    list_per_page = 20
admin.site.register(Evento, Eventos)

class Inscricoes (admin.ModelAdmin):
    list_display = ('id_inscricao','evento', 'aluno')
    list_display_links = ('id_inscricao',)
    search_fields = ('evento',)
    list_per_page = 20
admin.site.register(Inscricao, Inscricoes)

