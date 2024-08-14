from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from app.models import clientes



class ClientesListView(ListView):
    model = clientes
    context_object_name = "clientes"
    template_name = "vbc/lista_clientes.html"

class ClientesDeleteView(DeleteView):
    model = clientes
    template_name = "vbc/clientes_borrar.html"
    success_url = reverse_lazy('ClienteBorrar')

class ClientesUpdateView(UpdateView):
    model = clientes
    template_name = "vbc/actualiza_clientes.html"
    success_url = reverse_lazy('ListarClientes')
    fields = ["nombre","apellido"]