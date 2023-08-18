from django import forms

class Articulo_formulario(forms.Form):
    #Ver de que aparezca automatico el autor basado en el ID
    titulo = forms.CharField(max_length=50, label='', widget=forms.TextInput(attrs={'placeholder': 'Titulo','class':'form-control'}))
    subtitulo = forms.CharField(max_length=50, label='', widget=forms.TextInput(attrs={'placeholder': 'Subtitulo','class':'form-control'}))
    cuerpo = forms.CharField(label='', widget=forms.Textarea(attrs={'placeholder': 'Cuerpo','class':'form-control'}))
    fecha = forms.DateField(widget=forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}))

    



