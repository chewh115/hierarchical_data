from django import forms
from mptt.forms import TreeNodeChoiceField
from .models import Files

class FilesForm(forms.Form):
    name = forms.CharField(max_length=100)
    parent = TreeNodeChoiceField(queryset=Files.objects.all())