from django.shortcuts import render,redirect,HttpResponse
from django.http import JsonResponse
from django.views.generic import CreateView
#from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from .forms import RegistroForm
from .models import Cliente
from django.views.generic.edit import FormView

# Create your views here.

def agregarCliente(request):
    return render(request,'cliente/acliente.html')

def RegistroCliente(request):
    # form=RegistroForm()
    # return render(request,'cliente/registro.html',{'form':form})
    if request.method=="POST":
        form = RegistroForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("Exito al crear cliente")
    else:
        form = RegistroForm()
    return render(request,'cliente/registro.html',{'form':form})



    #     nombre=request.POST.get("nombre")
    #     direccion=request.POST.get("direccion")
    #     comuna = request.POST.get("comuna")
    #     correo= request.POST.get("correo")
    #     cliente = Cliente.objects.create(nombre=nombre,direccion=direccion,comuna=comuna,correo=correo)
    #     return HttpResponse("creado exitoso")
    # else:
    #     return HttpResponse("Invalid data")   

# class RegistroCliente(CreateView):
#     template_name="cliente/registro.html"

#     model = Cliente
    
#     form_class=RegistroForm
#     succes_url=reverse_lazy('apicliente')
    
    
    # def get(self, request):
    #     form=RegistroForm
    #     return render(request,self.template_name,{'form':form})
    # def post(self,request):
    #     form=RegistroForm(request.POST)   
    #     if form.is_valid():
    #         form.save()
    #         text = form.cleaned_data['post'] 
    #         form = RegistroForm
    #         return redirect['cliente:cliente']
    #     args = {'form':form,'text':text}
    #     return render(request,self.template_name, args)    