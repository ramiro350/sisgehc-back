from django.contrib import admin

from sisgehc.models import Aluno, Curso, Professor, Evento, Inscricao

class Alunos(admin.ModelAdmin):
    list_display = ('id','nome', 'matricula', 'horasComplementares', 'curso')
    list_display_links = ('id', 'nome')
    search_fields = ('nome',)
    list_per_page = 20
admin.site.register(Aluno, Alunos)

class Cursos (admin.ModelAdmin):
    list_display = ('id','nome')
    list_display_links = ('id', 'nome')
    search_fields = ('nome',)
    list_per_page = 20
admin.site.register(Curso, Cursos)

class Professores(admin.ModelAdmin):
    list_display = ('id','nome', 'matricula', 'curso', 'senha')
    list_display_links = ('id', 'nome')
    search_fields = ('nome',)
    list_per_page = 20
admin.site.register(Professor, Professores)

class Eventos (admin.ModelAdmin):
    list_display = ('id','nome', 'professor', 'curso', 'responsavel', 'horasComplementares', 'dataInicio', 'dataFim', 'horaInicio', 'horaFim', 'descricao', 'imagem')
    list_display_links = ('id', 'nome')
    search_fields = ('nome',)
    list_per_page = 20
admin.site.register(Evento, Eventos)

class Inscricoes (admin.ModelAdmin):
    list_display = ('id','evento', 'Aluno')
    list_display_links = ('id',)
    search_fields = ('evento',)
    list_per_page = 20
admin.site.register(Inscricao, Inscricoes)