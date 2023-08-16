from django import forms 

class CreateNewTask(forms.Form):
    #solo necesitamos agregar titulo y descripcion
    title = forms.CharField(label="Titulo de tarea", max_length=200, widget=forms.TextInput(attrs={'class':'input'}))
    description = forms.CharField(label="Descripción", widget=forms.Textarea(attrs={'class':'input'}))

#Clase para crear Project
class CreateNewProject(forms.Form):
    name = forms.CharField(label="Nombre del Proyecto", max_length=300, widget=forms.TextInput(attrs={'class':'input'}))