from django import forms
from.models import Task 
# Reordering Form and View

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = "__all__" 

