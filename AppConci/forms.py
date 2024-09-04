from django import forms
from AppConci.models import Cliente, Tractor, Cosechadora

class clienteFormulario(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['nombre_completo', 'cuit', 'email', 'telefono', 'localidad' ]
        # nombre_completo = forms.CharField(max_length=50)
        # cuit = forms.IntegerField()
        # email = forms.EmailField()
        # telefono = forms.CharField()
        # localidad = forms.CharField(max_length=50)

class tractoresFormulario(forms.ModelForm):
    class Meta:
        model = Tractor
        fields = ['familia', 'modelo', 'serie']

        # familia = forms.CharField(max_length=30)
        # modelo = forms.CharField(max_length=30)
        # serie = forms.CharField(max_length=30)

class cosechadorasFormulario(forms.ModelForm):
    class Meta:
        model = Cosechadora
        fields = ['familia', 'modelo', 'serie']
        # familia = forms.CharField(max_length=30)
        # modelo = forms.CharField(max_length=30)
        # serie = forms.CharField(max_length=30)

# class SearchForm(forms.Form):
#     query = forms.CharField(label='Concepto', max_length=100)

class SearchForm(forms.Form):
    query = forms.CharField(
        label='Concepto',
        required=True,
        error_messages={'required': 'Este campo es obligatorio'}
    )