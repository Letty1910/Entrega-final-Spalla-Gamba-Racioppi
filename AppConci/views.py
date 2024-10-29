from django.views.generic import TemplateView, ListView, DetailView, UpdateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView 
from django.contrib.auth.views import LoginView, PasswordChangeView
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.contrib.auth import login, logout
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from .models import MaquinaAgricola, Comentario
from .forms import (
    FormularioNuevaMaquina, ActualizacionMaquinaAgricola, FormularioCambioPassword, 
    FormularioEdicion, FormularioNuevaMaquina, FormularioRegistroUsuario, FormularioComentario
)

class HomeView(LoginRequiredMixin, TemplateView):
    template_name = 'AppConci/home.html'

class LoginPagina(LoginView):
    template_name = 'AppConci/login.html'
    fields = 'all'
    redirect_authenticated_user = True
    success_url = reverse_lazy('home')

    def get_success_url(self):
        return reverse_lazy('home')

class RegistroPagina(FormView):
    template_name = 'AppConci/registro.html'
    form_class = FormularioRegistroUsuario
    redirect_authenticated_user = True
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
    template_name = 'AppConci/edicionPerfil.html'
    success_url = reverse_lazy('home')

    def get_object(self):
        return self.request.user

class CambioPassword(PasswordChangeView):
    form_class = FormularioCambioPassword
    template_name = 'AppConci/passwordCambio.html'
    success_url = reverse_lazy('password_exitoso')

def password_exitoso(request):
    return render(request, 'AppConci/passwordExitoso.html', {})


# COSECHADORA

class CosechadoraLista(LoginRequiredMixin, ListView):
    context_object_name = 'cosechadoras'
    queryset = MaquinaAgricola.objects.filter(maquina__startswith='cosechadora')
    template_name = 'AppConci/listaCosechadora.html'
    login_url = '/login/'

class CosechadoraDetalle(LoginRequiredMixin, DetailView):
    model = MaquinaAgricola
    context_object_name = 'cosechadora'
    template_name = 'AppConci/cosechadoraDetalle.html'

class CosechadoraUpdate(LoginRequiredMixin, UpdateView):
    model = MaquinaAgricola
    form_class = ActualizacionMaquinaAgricola
    success_url = reverse_lazy('lista_cosechadora')
    context_object_name = 'cosechadora'
    template_name = 'AppConci/cosechadoraEdicion.html'

class CosechadoraDelete(LoginRequiredMixin, DeleteView):
    model = MaquinaAgricola
    success_url = reverse_lazy('lista_cosechadora')
    context_object_name = 'cosechadora'
    template_name = 'AppConci/cosechadoraBorrado.html'

# TRACTOR

class TractorLista(LoginRequiredMixin, ListView):
    context_object_name = 'tractores'
    queryset = MaquinaAgricola.objects.filter(maquina='Tractores')
    template_name = 'AppConci/listaTractor.html'

class TractorDetalle(LoginRequiredMixin, DetailView):
    model = MaquinaAgricola
    context_object_name = 'tractor'
    template_name = 'AppConci/tractorDetalle.html'

class TractorUpdate(LoginRequiredMixin, UpdateView):
    model = MaquinaAgricola
    form_class = ActualizacionMaquinaAgricola
    success_url = reverse_lazy('lista_tractor')
    context_object_name = 'tractor'
    template_name = 'AppConci/tractorEdicion.html'

class TractorDelete(LoginRequiredMixin, DeleteView):
    model = MaquinaAgricola
    success_url = reverse_lazy('lista_tractor')
    context_object_name = 'tractor'
    template_name = 'AppConci/tractorBorrado.html'


# OTRO

class OtroLista(LoginRequiredMixin, ListView):
    context_object_name = 'otros'
    queryset = MaquinaAgricola.objects.filter(maquina__startswith='otro')
    template_name = 'AppConci/listaOtros.html'

class OtroDetalle(LoginRequiredMixin, DetailView):
    model = MaquinaAgricola
    context_object_name = 'otro'
    template_name = 'AppConci/otroDetalle.html'

class OtroUpdate(LoginRequiredMixin, UpdateView):
    model = MaquinaAgricola
    form_class = ActualizacionMaquinaAgricola
    success_url = reverse_lazy('lista_otros')
    context_object_name = 'otro'
    template_name = 'AppConci/otroEdicion.html'

class OtroDelete(LoginRequiredMixin, DeleteView):
    model = MaquinaAgricola
    success_url = reverse_lazy('lista_otros')
    context_object_name = 'otro'
    template_name = 'AppConci/otroBorrado.html'

# CREACION DE MAQUINARIA

class MaquinaCreacion(LoginRequiredMixin, CreateView):
    model = MaquinaAgricola
    form_class = FormularioNuevaMaquina
    success_url = reverse_lazy('lista_tractor')
    template_name = 'AppConci/maquinaCreacion.html'

    def form_valid(self, form):
        form.instance.usuario = self.request.user 
        return super(MaquinaCreacion, self).form_valid(form)

# COMENTARIOS

class ComentarioPagina(LoginRequiredMixin, CreateView):
    model = Comentario
    form_class = FormularioComentario
    template_name = 'AppConci/comentario.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        form.instance.maquina_id = self.kwargs['pk']
        return super(ComentarioPagina, self).form_valid(form)

# ACERCA DE MI

def about(request):
    return render(request, 'AppConci/acercaDeMi.html', {})
