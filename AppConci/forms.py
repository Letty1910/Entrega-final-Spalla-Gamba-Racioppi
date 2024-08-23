from django import forms    
class clienteFormulario(forms.Form):
    nombre_completo = forms.CharField(max_length=50)
    cuit = forms.IntegerField()
    email = forms.EmailField()
    localidad = forms.CharField(max_length=50)

class tractoresFormulario(forms.Form):
    familia = forms.CharField(max_length=30)
    modelo = forms.CharField(max_length=30)
    serie = forms.CharField(max_length=30)

class cosechadorasFormulario(forms.Form):
    familia = forms.CharField(max_length=30)
    modelo = forms.CharField(max_length=30)
    serie = forms.CharField(max_length=30)

class ventasFormulario(forms.Form):
    cuit = forms.IntegerField()
    fecha_de_venta = forms.DateField()
    entregado = forms.BooleanField()  