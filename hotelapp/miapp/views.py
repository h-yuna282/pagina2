from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from django.urls import reverse_lazy
from .models import *
from django.http import HttpResponseRedirect
from .forms import pagoForm,detalle_pagoFormSet

# Create your views here.
def index(request):
    return render(request, "miapp/index.html")

class habitacionList(ListView):
    model = habitacion
    template_name = "miapp/Listarhabitacion.html"

class habitacionDetalle(DetailView):
    model = habitacion
    template_name = 'miapp/detallehabitacion.html'

class habitacionCreate(CreateView):
    model = habitacion
    fields = ['num_habitacion','estado','precio','tipo_de_habitacion']
    template_name = 'miapp/nuevohabitacion.html'
    success_url = reverse_lazy('Listarhabitacion')

class habitacionUpdate(UpdateView):
    model = habitacion
    fields = ['num_habitacion','estado','precio','tipo_de_habitacion']
    template_name = 'miapp/editarhabitacion.html'
    success_url = reverse_lazy('Listarhabitacion')

class habitacionDelete(DeleteView):
    model = habitacion
    template_name = 'miapp/eliminarhabitacion.html'
    success_url = reverse_lazy('Listarhabitacion')

class clienteCreate(CreateView):
    model = cliente
    fields = ['nombre','apellido','dni','domicilio','sexo','telefono','mail']
    template_name = 'miapp/nuevocliente.html'
    success_url = reverse_lazy('Listarhabitacion')

class pagoList(ListView):
    model = pago
    template_name = 'miapp/lista_pago.html'

class pagoCreate(CreateView):
    model = pago
    form_class = pagoForm    
    template_name = 'miapp/nuevo_pago.html'
    success_url = reverse_lazy('lista_pago')

    #A partir de aqui vamos a usar dos metodos que son get y post, cada uno se ejecuta segun las peticiones que llegan del navegador
    #Cuando en ese mismo formulario se envian datos, esos datos se envian como POST y en ese caso se ejecuta el metodo post de esta vista que permita almacenar los datos del pago y su detalle

    # se ejecuta solo cuando se va a mostrar la pagina nuevo_pago.html sin enviar datos al servidor
    def get(self, request, *args, **kwargs):
            
        self.object = None
        #Instanciamos el formulario de pagoForm que declaramos en la variable form_class
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        #Instanciamos el formset, el formset se llama detalle_pagoFormSet y es un formulario personalizado para detalle_pago,
        #se encuentra en el archivo forms.py, el modelo pago tambien tiene un formulario personalizado en el archivo forms.py
        detalle_orden_pago_formset=detalle_pagoFormSet()
        
        #Renderizamos el formulario de pagos y el formset 
        return self.render_to_response(self.get_context_data(form=form,
                                                            detalle_pago_form_set=detalle_orden_pago_formset))
    # se ejecuta solo cuando se da click en el boton enviar creando el pago (Se envian datos al servidor)
    def post(self, request, *args, **kwargs):
        
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        #Obtenemos el formset pero ya con lo que se le pasa en el POST (Los datos del detalle)
        detalle_pago_form_set = detalle_pagoFormSet(request.POST)
        
        #Llamamos a los métodos para validar el formulario de Compra y el formset, si son válidos ambos se llama al método
        #form.valid() o en caso contrario se llama al método form_invalid()
        
        if form.is_valid() and detalle_pago_form_set.is_valid():
            return self.form_valid(form, detalle_pago_form_set)
        else:
            return self.form_invalid(form, detalle_pago_form_set)

    def form_valid(self, form, detalle_pago_form_set):

        #Aquí ya guardamos el object de acuerdo a los valores del formulario de pago
        self.object = form.save()
        #Utilizamos el atributo instance del formset para asignarle el valor del objeto pago creado y que nos indica el modelo Foráneo
        detalle_pago_form_set.instance = self.object
        #Finalmente guardamos el formset para que tome los valores que tiene
        detalle_pago_form_set.save()
        #Redireccionamos a la ventana del listado de pagos
        return HttpResponseRedirect(self.success_url)

    def form_invalid(self, form, detalle_pago_form_set):
        #Si es inválido el form de pago o el formset renderizamos los errores
        return self.render_to_response(self.get_context_data(form=form,detalle_pago_form_set = detalle_pago_form_set))

