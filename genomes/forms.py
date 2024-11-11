from django import forms
from .models import Genome

class GenomeForm(forms.Form):
    sequence_id = forms.CharField(max_length=100, label='Sequence ID')
    sequence = forms.CharField(widget=forms.Textarea, label='Sequence')
    description = forms.CharField(widget=forms.Textarea, label='Description', required=False)

class GenomeEditForm(forms.ModelForm):
    class Meta:
        model = Genome
        fields = ['sequence_id', 'description']