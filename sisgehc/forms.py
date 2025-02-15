from django import forms
from .models import AtividadeComplementar

class AtividadeComplementarForm(forms.ModelForm):
    class Meta:
        model = AtividadeComplementar
        fields = ['aluno', 'carga_horaria', 'coordenador', 'data_submissao', 
                  'data_validacao', 'arquivo_certificacao', 'tipo_atividade', 
                  'sub_tipo', 'area_de_conhecimento']
