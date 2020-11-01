from django.shortcuts import render
from .models import SliderIndex,Insumos,MisionyVision,Galeria

from django.contrib.auth.models import User
from django.contrib.auth import authenticate, logout, login as login_autent
from django.contrib.auth.decorators import login_required,permission_required
# Create your views here.

def index(request):
    sliders = SliderIndex.objects.all()
    return render(request,'web/index2.html',{'imagenes':sliders})

def galeria(request):
    foto = Galeria.objects.all()
    return render(request,'web/galeria2.html',{'imagenes':foto})

def ubicacion(request):
    return render(request,'web/ubicacion2.html')

def mision_vision(request):
    lista = MisionyVision.objects.all()    
    return render(request,'web/mision_vision2.html',{'lista':lista})

@login_required(login_url='/login/')
@permission_required('auth.add_user',login_url='/login/')
def registro(request):
    if request.POST:
        nombre = request.POST.get("txtNombre")
        apellido = request.POST.get("txtApellido")
        email = request.POST.get("txtEmail")
        usu = request.POST.get("txtNombreusuario")
        password = request.POST.get("txtPass1")
        pass2 = request.POST.get("txtPass2")
        if password!=pass2:
            return render(request,'web/registro2.html',{'msg':'Claves incorrectas'})
        try:
            usuario = User.objects.get(username=usu)
            return render(request,'web/registro2.html',{'msg':'Usuario existe'})
        except:                        
            usuario = User()
            usuario.first_name = nombre
            usuario.last_name = apellido
            usuario.email = email
            usuario.username = usu
            usuario.set_password(password)

            usuario.save()

            usuario = authenticate(request,username=usuario, password=password)
            login_autent(request,usuario)
            sliders = SliderIndex.objects.all()
            return render(request,'web/index2.html',{'imagenes':sliders})


    return render(request,'web/registro2.html')

@login_required(login_url='/login/')
@permission_required('myCar.view_insumos',login_url='/login/')
@permission_required('myCar.delete_insumos',login_url='/login/')
def eliminar_insumo(request,id):
    try:
        insumo = Insumos.objects.get(nombre=id)
        insumo.delete()
        msg='Elimino Insumo'
    except:
        msg='No Elimino'
    lista = Insumos.objects.all()
    return render(request,'web/admin_formulario_insumos.html',{'listar_insumos':lista, 'msg':msg})
     


@login_required(login_url='/login/')
@permission_required('myCar.view_insumos',login_url='/login/')
def lista_insumos(request):
    lista = Insumos.objects.all()
    return render(request,'web/admin_formulario_insumos.html',{'listar_insumos':lista})

@login_required(login_url='/login/')
@permission_required('myCar.change_insumos',login_url='/login/')
def modificar(request):
    if request.POST:
        nombre = request.POST.get("txtProducto")
        precio = request.POST.get("txtPrecio")
        descripcion = request.POST.get("txtDescripcion")
        stock = request.POST.get("txtStock")

        try:
            insumo = Insumos.objects.all(nombre=nombre)
            insumo.precio = precio
            insumo.descripcion = descripcion
            insumo.stock = stock
            insumo.save()
            msg = 'Modifico'
        except:
            msg = 'No Modifico'
    lista = Insumos.objects.all()
    return render(request,'web/admin_formulario_insumos.html',{'listar_insumos':lista, 'msg':msg})


       
@login_required(login_url='/login/')
@permission_required('myCar.view_insumos',login_url='/login/')
def buscar(request,id):
    try:
        insumo = Insumos.objects.get(nombre=id)
        return render(request,'web/formulario_insumo_mod.html',{'insumo':insumo})
    except:
        msg='no existe insumo'
    lista = Insumos.objects.all()
    return render(request,'web/admin_formulario_insumos.html',{'listar_insumos':lista, 'msg':msg})


@login_required(login_url='/login/')
@permission_required('myCar.add_insumos',login_url='/login/')
@permission_required('myCar.change_insumos',login_url='/login/')
def formulario_insumos(request):
    if request.POST:
        nombre = request.POST.get("txtProducto")
        precio = request.POST.get("txtPrecio")
        descripcion = request.POST.get("txtDescripcion")
        stock = request.POST.get("txtStock")

        insumo = Insumos(
            nombre=nombre,
            precio=precio,
            descripcion=descripcion,
            stock=stock
        )

        insumo.save()
        return render(request,'web/formulario_insumos2.html',{'msg':'Grabo insumo'})
    return render(request,'web/formulario_insumos2.html')

def login (request):
    if request.POST:
        usuario = request.POST.get("txtNombreusuario")
        password = request.POST.get("txtPass1")
        usuario = authenticate(request,username=usuario, password=password)
        if usuario is not None and usuario.is_active:
            login_autent(request,usuario)
            sliders = SliderIndex.objects.all()
            return render(request,'web/index2.html',{'imagenes':sliders})
        else:
            return render(request,'web/login2.html', {'msg':'no existe usuario'})
    return render(request,'web/login2.html')

def cerrar (request):
    logout(request)
    sliders = SliderIndex.objects.all()
    return render(request,'web/index2.html',{'imagenes':sliders})
