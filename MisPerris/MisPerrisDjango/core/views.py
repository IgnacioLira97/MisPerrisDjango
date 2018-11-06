# -*- coding: utf-8 -*- 
from django.shortcuts import render
from .models import Estado, Region, Ciudad, tipoVivienda, Raza, Usuario, Mascota
from django.shortcuts import render
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User


import sys
from itertools import cycle
import datetime
import smtplib
import shutil, os
from django.contrib import auth
import time


# Create your views here.
def home(request):
    mas=Mascota.objects.all()

    if  request.user.is_authenticated:
        na=request.user.is_staff
        if na ==True:
            return render(request,'core/home.html',{'perritos':mas,'ingresado':True,'na':na,'admin':True})
        else:
            return render(request,'core/home.html',{'perritos':mas,'ingresado':True,'na':na})


    else:
        return render(request,'core/home.html',{'perritos':mas,'deslog':True})

def actualizarMascota(request):
    user=Mascota.objects.all()
    raza=Raza.objects.all() #city
    estado=Estado.objects.all() #vivienda
    if request.POST:
        accion=request.POST.get("btnAccion","")
        mensaje=""
        if accion == "Buscar":
            id=request.POST.get("id","")
            pe=Mascota.objects.get(idMascota=id)
            mensaje="Encontro"
            return render(request,'core/actualizarMascota.html',{'razas':raza,'user':user,'estados':estado,'pe':pe,"mensaje":mensaje})
        if accion == "Modificar":
            idmasc=request.POST.get("id","")
            pe=Mascota.objects.get(idMascota=idmasc)
            nom=request.POST.get("nombre","")
            desc=request.POST.get("descripcion","")
            raza=request.POST.get("raza","")
            obj_raza=Raza.objects.get(Raza=raza)
            vivi=request.POST.get("estado","")
            obj_estado=Estado.objects.get(name=vivi)
            
            pe.name=nom
            pe.descripcion=desc
            pe.raza=obj_raza
            pe.idEstado=obj_estado
            pe.save()
            mensaje="Updated"

            return render(request,'core/actualizarMascota.html',{'razas':raza,'user':user,'estados':estado ,"mensaje":mensaje})
    return render(request,'core/actualizarMascota.html',{'razas':raza,'user':user,'estados':estado})

def eliminarMascotas(request):
    masc=Mascota.objects.all()
    resp=False
    if request.POST:
        id=request.POST.get("id","")
        mascota=Mascota.objects.get(idMascota=id)
        mascota.delete()
        resp=True
    return render(request,'core/eliminarMascotas.html',{'mascotas':masc,'respuesta':resp})

def listarMascota(request):
    masc=Mascota.objects.all()
    return render(request,'core/listarMascotas.html',{'mascotas':masc})

def agregarMascota(request):
    raza=Raza.objects.all()
    estado=Estado.objects.all()
    masc=Mascota.objects.all()
    resp=False
    if request.POST:
        id=request.POST.get("id","")
        name=request.POST.get("nombre","")
        foto=request.FILES.get("foto","")
        desc=request.POST.get("descripcion","")
        raza=request.POST.get("raza","")
        obj_raza=Raza.objects.get(Raza=raza)
        vivi=request.POST.get("estado","")
        obj_estado=Estado.objects.get(name=vivi)
        j=1
        for s in masc:
            j=j+1
        i=j+1
        masc=Mascota(
            idMascota=j,
            name=name,
            foto=foto,
            descripcion=desc,
            raza=obj_raza,
            idEstado=obj_estado
        )
        masc.save()
        resp=True

    return render(request,'core/agregarMascota.html',{'razas':raza,'estados':estado ,'respuesta':resp})


def actualizarPersona(request):
    user=Usuario.objects.all()
    city=Ciudad.objects.all()
    vivienda=tipoVivienda.objects.all()
    mensaje=""
    if request.POST:
        accion=request.POST.get("btnAccion","")
        
        if accion == "Buscar":
            run=request.POST.get("run","")
            pe=Usuario.objects.get(run=run)
            mensaje="Encontró"
            return render(request,'core/modificar_personas.html',{'ciudades':city,'user':user,'viviendas':vivienda,'pe':pe,"mensaje":mensaje})
        if accion == "Modificar":
            run=request.POST.get("run","")
            usu=request.POST.get("usuario","")
            pe=Usuario.objects.get(run=run)
            nom=request.POST.get("nombre","")
            correo=request.POST.get("correo","")
            fecha=request.POST.get("fecha","")
            telefono=request.POST.get("telefono","")
            #contrasena=request.POST.get("password","")
            region=request.POST.get("region","")
            ciudad=request.POST.get("comuna","")
            vivi=request.POST.get("vivienda","")
            obj_vivienda=tipoVivienda.objects.get(tipo=vivi)

            
            pe.run=run
            pe.usuario=usu
            pe.nombre=nom
            pe.correo=correo
            pe.fechaNacimiento=fecha
            pe.telefono=telefono
            #pe.password=contrasena,
            pe.region=region
            pe.comuna=ciudad
            pe.tipoVivienda=obj_vivienda
            pe.save()
            mensaje="Updated"

            return render(request,'core/modificar_personas.html',{'ciudades':city,'user':user,'viviendas':vivienda ,"mensaje":mensaje})
    return render(request,'core/modificar_personas.html',{'ciudades':city,'user':user,'viviendas':vivienda, "mensaje":mensaje})



def eliminarPersona(request):
    peli=Usuario.objects.all()
    resp=False
    if request.POST:
        var=request.POST.get("run","")
        pel=Usuario.objects.get(run=var)
        pel.delete()
        resp=True
    return render(request,'core/eliminar_persona.html',{'personas':peli,'respuesta':resp})

def listarPersona(request):
    per=Usuario.objects.all()
    return render(request,'core/listar_personas.html',{'personas':per})


def agregarPersona(request):
    vivienda=tipoVivienda.objects.all()
    resp=False
    if request.POST:
        run=request.POST.get("run","")
        usu=request.POST.get("usuario","")
        nom=request.POST.get("nombre","")
        correo=request.POST.get("correo","")
        fecha=request.POST.get("fecha","")
        telefono=request.POST.get("telefono","")
        contrasena=request.POST.get("password","")
        region=request.POST.get("region","")
        ciudad=request.POST.get("comuna","")
        #obj_ciudad=Ciudad.objects.get(name=ciudad)
        vivi=request.POST.get("vivienda","")
        obj_vivienda=tipoVivienda.objects.get(tipo=vivi)
        per=Usuario(
            run=run,
            nombre=nom,
            usuario=usu,
            correo=correo,
            fechaNacimiento=fecha,
            telefono=telefono,
            password=contrasena,
            region=region,
            ciudad=ciudad,
            tipoVivienda=obj_vivienda
        )
        per.save()
        resp=True

    return render(request,'core/formulario.html',{'viviendas':vivienda ,'respuesta':resp})

def logout(request):
    pe=Mascota.objects.all()
    auth.logout(request)
    return render(request,'core/home.html',{'perritos':pe,'deslog':True})

def login(request):
    usus=User.objects.all()
    pe=Mascota.objects.all()
    
    if request.POST:

        user=request.POST.get("txtUsuario","")
        passa=request.POST.get("txtPass","")
        user=auth.authenticate(username=user,password=passa)
        if user is not None and user.is_active:
            auth.login(request,user)
            na=request.user.is_staff
            if na == True :
                pe=Mascota.objects.all()
                return render(request,'core/home.html',{'ingresado':True,'pe':pe,'admin':True})
            else:
                pe=Mascota.objects.all()
                return render(request,'core/home.html',{'ingresado':True,'pe':pe})
            
        else:
            return render(request,'core/login.html',{'error':True})
        

    else:
        return render(request,'core/login.html')

def recuperar(request):

    if request.POST:
        exs=request.POST.get("txtUsuario")
        try:
            user=Usuario.objects.get(usuario=exs)
        except Exception as ex:
            return render(request,'core/recuperar.html',{'noexiste':True})
        us=user.usuario
        password=user.password
        email=user.correo
        mssg="Hola "+us+", nuestro sistema no acaba de indicar que ha perdido su password. Su password para poder acceder al sistema es: "+password+". No la comparta con nadie."
        remitente = 'misperris.no.reply@gmail.com'
        destinatario  = email
        mensaje = mssg
        usuario = 'misperris.no.reply@gmail.com'
        clave = 'w1w2w3w4w5'
        server = smtplib.SMTP('smtp.gmail.com:587')
        server.starttls()
        server.login(usuario,clave)
        server.sendmail(remitente,destinatario,mensaje.encode())
        server.quit()

        return render(request,'core/recuperar.html',{'correo':email})
    else:
        return render(request,'core/recuperar.html')


def servicios(request):
    return render(request,'core/servicios.html')
    
def menu(request):
    return render(request,'core/menu.html')

def menu_perros(request):
    return render(request, 'core/menu_perros.html')
def menu_persona(request):
    return render(request, 'core/menu_persona.html')

def galeria(request):
    return render(request, 'core/galeria.html')


def regPersona(request):
    vivienda=tipoVivienda.objects.all()
    resp=False
    if request.POST:
        run=request.POST.get("run","")
        usu=request.POST.get("usuario","")
        nom=request.POST.get("nombre","")
        correo=request.POST.get("correo","")
        fecha=request.POST.get("fecha","")
        telefono=request.POST.get("telefono","")
        contrasena=request.POST.get("password","")
        region=request.POST.get("region","")
        ciudad=request.POST.get("comuna","")
        #obj_ciudad=Ciudad.objects.get(name=ciudad)
        vivi=request.POST.get("vivienda","")
        obj_vivienda=tipoVivienda.objects.get(tipo=vivi)
        per=Usuario(
            run=run,
            nombre=nom,
            usuario=usu,
            correo=correo,
            fechaNacimiento=fecha,
            telefono=telefono,
            password=contrasena,
            region=region,
            ciudad=ciudad,
            tipoVivienda=obj_vivienda
        )
        per.save()
        resp=True

    return render(request,'core/reg.html',{'viviendas':vivienda ,'respuesta':resp})