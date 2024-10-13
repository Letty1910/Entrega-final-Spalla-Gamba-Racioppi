from django.views.generic import TemplateView, ListView, DetailView, UpdateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView 
from django.contrib.auth.views import LoginView, PasswordChangeView
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.contrib.auth import login
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from .models import MaquinaAgricola, Comentario
from .forms import ActualizacionMaquina, FormularioCambioPassword, FormularioEdicion, FormularioNuevaMaquina, FormularioRegistroUsuario, FormularioComentario


class HomeView(LoginRequiredMixin, TemplateView):
    template_name = 'appconci/home.html'

class LoginPagina(LoginView):
    template_name = 'appconci/login.html'
    fields = '__all__'
    redirect_autheticated_user = True
    success_url = reverse_lazy('home')

    def get_success_url(self):
        return reverse_lazy('home')

class RegistroPagina(FormView):
    template_name = 'appconci/registro.html'
    form_class = FormularioRegistroUsuario
    redirect_autheticated_user = True
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        user = form.save()
        if user is not None:
            login(self.request, user)
        return super(RegistroPagina, self).form_valid(form)

    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('home')
        return super(RegistroPagina, self).get(*args, **kwargs)

class UsuarioEdicion(UpdateView):
    form_class = FormularioEdicion
    template_name= 'appconci/edicionPerfil.html'
    success_url = reverse_lazy('home')

    def get_object(self):
        return self.request.user

class CambioPassword(PasswordChangeView):
    form_class = FormularioCambioPassword
    template_name = 'appconci/passwordCambio.html'
    success_url = reverse_lazy('password_exitoso')

def password_exitoso(request):
    return render(request, 'appconci/passwordExitoso.html', {})


# TRACTORES

class TractorLista(LoginRequiredMixin, ListView):
    context_object_name = 'tractores'
    queryset = MaquinaAgricola.objects.filter(maquina__startswith='Tractores')
    template_name = 'appconci/listaTractores.html'
    login_url = '/login/'

class TractorDetalle(LoginRequiredMixin, DetailView):
    model = MaquinaAgricola
    context_object_name = 'tractor'
    template_name = 'appconci/tractorDetalle.html'

class TractorUpdate(LoginRequiredMixin, UpdateView):
    model = MaquinaAgricola
    form_class = ActualizacionMaquina
    success_url = reverse_lazy('tractores')
    context_object_name = 'tractor'
    template_name = 'appconci/tractorEdicion.html'

class TractorDelete(LoginRequiredMixin, DeleteView):
    model = MaquinaAgricola
    success_url = reverse_lazy('tractores')
    context_object_name = 'tractor'
    template_name = 'appconci/tractorBorrado.html'

# COSECHADORA

class CosechadoraLista(LoginRequiredMixin, ListView):
    context_object_name = 'bajos'
    queryset = MaquinaAgricola.objects.filter(maquina__startswith='Cosechadoras')
    template_name = 'appconci/listaCosechadoras.html'

class CosechadoraDetalle(LoginRequiredMixin,DetailView):
    model = MaquinaAgricola
    context_object_name = 'bajo'
    template_name = 'appconci/cosechadoraDetalle.html'

class CosechadoraUpdate(LoginRequiredMixin, UpdateView):
    model = MaquinaAgricola
    form_class = ActualizacionMaquina
    success_url = reverse_lazy('cosechadoras')
    context_object_name = 'cosechadora'
    template_name = 'appconci/cosechadoraEdicion.html'

class CosechadoraDelete(LoginRequiredMixin, DeleteView):
    model = MaquinaAgricola
    success_url = reverse_lazy('cosechadoras')
    context_object_name = 'cosechadora'
    template_name = 'appconci/cosechadoraBorrado.html'

# # OTRO

# class OtroLista(LoginRequiredMixin, ListView):
#     context_object_name = 'otros'
#     queryset = Instrumento.objects.filter(instrumento__startswith='otro')
#     template_name = 'appconci/listaOtros.html'

# class OtroDetalle(LoginRequiredMixin, DetailView):
#     model = Instrumento
#     context_object_name = 'otro'
#     template_name = 'appconci/otroDetalle.html'

# class OtroUpdate(LoginRequiredMixin, UpdateView):
#     model = Instrumento
#     form_class = ActualizacionInstrumento
#     success_url = reverse_lazy('otros')
#     context_object_name = 'otro'
#     template_name = 'appconci/otroEdicion.html'

# class OtroDelete(LoginRequiredMixin, DeleteView):
#     model = Instrumento
#     success_url = reverse_lazy('otros')
#     context_object_name = 'otro'
#     template_name = 'appconci/otroBorrado.html'

# CREACION MAQUINA

class MaquinaCreacion(LoginRequiredMixin, CreateView):
    model = MaquinaAgricola
    form_class = FormularioNuevaMaquina
    success_url = reverse_lazy('appconci')
    template_name = 'appconci/maquinaCreacion.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(MaquinaCreacion, self).form_valid(form)

# COMENTARIOS

class ComentarioPagina(LoginRequiredMixin, CreateView):
    model = Comentario
    form_class = FormularioComentario
    template_name = 'appconci/comentario.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        form.instance.comentario_id = self.kwargs['pk']
        return super(ComentarioPagina, self).form_valid(form)

# ACERCA DE MI

def about(request):
    return render(request, 'appconci/AcercaDeMi.html', {})