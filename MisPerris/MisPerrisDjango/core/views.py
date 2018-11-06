from django.shortcuts import render
from .models import Estado, Region, Ciudad, tipoVivienda, Raza, User, Mascota
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
    # return render(request,'core/home.html') 
    mas=Mascota.objects.all()
    
    if  request.user.is_authenticated:
        na=request.user.is_staff
        if na ==True:
            return render(request,'core/home.html',{'perritos':mas,'ingresado':True,'na':na,'admin':True})
        else:
            return render(request,'core/home.html',{'perritos':mas,'ingresado':True,'na':na})
        

    else:
        return render(request,'core/home.html',{'perritos':mas,'deslog':True})

@login_required
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
            pic=request.POST.get("foto","")
            desc=request.POST.get("descripcion","")
            raza=request.POST.get("raza","")
            obj_raza=Raza.objects.get(Raza=raza)
            vivi=request.POST.get("estado","")
            obj_estado=Estado.objects.get(name=vivi)
            
            pe.name=nom
            pe.foto=pic
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
    resp=False
    if request.POST:
        id=request.POST.get("id","")
        name=request.POST.get("nombre","")
        foto=request.POST.get("foto","")
        desc=request.POST.get("descripcion","")
        raza=request.POST.get("raza","")
        obj_raza=Raza.objects.get(Raza=raza)
        vivi=request.POST.get("estado","")
        obj_estado=Estado.objects.get(name=vivi)
        masc=Mascota(
            idMascota=id,
            name=name,
            foto=foto,
            descripcion=desc,
            raza=obj_raza,
            idEstado=obj_estado
        )
        masc.save()
        resp=True
    else:
        na=request.user.is_staff
        if na == True:
            return render(request,'core/agregarMascota.html',{'razas':raza,'estados':estado ,'respuesta':resp})
        else:
            raza=Raza.objects.all()
            return render(request,'core/home.html',{'ingresado':True,'raza':raza})
    


def actualizarPersona(request):
    user=User.objects.all()
    city=Ciudad.objects.all()
    vivienda=tipoVivienda.objects.all()
    mensaje=""
    if request.POST:
        accion=request.POST.get("btnAccion","")
        
        if accion == "Buscar":
            run=request.POST.get("run","")
            pe=User.objects.get(run=run)
            mensaje="Encontró"
            return render(request,'core/modificar_personas.html',{'ciudades':city,'user':user,'viviendas':vivienda,'pe':pe,"mensaje":mensaje})
        if accion == "Modificar":
            run=request.POST.get("run","")
            pe=User.objects.get(run=run)
            nom=request.POST.get("nombre","")
            correo=request.POST.get("correo","")
            fecha=request.POST.get("fecha","")
            telefono=request.POST.get("telefono","")
            #contrasena=request.POST.get("password","")
            ciudad=request.POST.get("ciudad","")
            obj_ciudad=Ciudad.objects.get(name=ciudad)
            vivi=request.POST.get("vivienda","")
            obj_vivienda=tipoVivienda.objects.get(tipo=vivi)

            
            pe.run=run
            pe.nombre=nom
            pe.correo=correo
            pe.fechaNacimiento=fecha
            pe.telefono=telefono
            #pe.password=contrasena,
            pe.idCiudad=obj_ciudad
            pe.tipoVivienda=obj_vivienda
            pe.save()
            mensaje="Updated"

            return render(request,'core/modificar_personas.html',{'ciudades':city,'user':user,'viviendas':vivienda ,"mensaje":mensaje})
    return render(request,'core/modificar_personas.html',{'ciudades':city,'user':user,'viviendas':vivienda, "mensaje":mensaje})

def eliminarPersona(request):
    peli=User.objects.all()
    resp=False
    if request.POST:
        var=request.POST.get("run","")
        pel=User.objects.get(run=var)
        pel.delete()
        resp=True
    return render(request,'core/eliminar_persona.html',{'personas':peli,'respuesta':resp})

def listarPersona(request):
    per=User.objects.all()
    return render(request,'core/listar_personas.html',{'personas':per})

def agregarPersona(request):
    city=Ciudad.objects.all()
    vivienda=tipoVivienda.objects.all()
    resp=False
    if request.POST:
        run=request.POST.get("run","")
        nom=request.POST.get("nombre","")
        correo=request.POST.get("correo","")
        fecha=request.POST.get("fecha","")
        telefono=request.POST.get("telefono","")
        contrasena=request.POST.get("password","")
        ciudad=request.POST.get("ciudad","")
        obj_ciudad=Ciudad.objects.get(name=ciudad)
        vivi=request.POST.get("vivienda","")
        obj_vivienda=tipoVivienda.objects.get(tipo=vivi)
        per=User(
            run=run,
            nombre=nom,
            correo=correo,
            fechaNacimiento=fecha,
            telefono=telefono,
            password=contrasena,
            idCiudad=obj_ciudad,
            tipoVivienda=obj_vivienda
        )
        per.save()
        resp=True

    return render(request,'core/formulario.html',{'ciudades':city,'viviendas':vivienda ,'respuesta':resp})

def logout(request):
    pe=Mascota.objects.all()
    auth.logout(request)
    return render(request,'core/home.html',{'perritos':pe,'deslog':True})

def login(request):
    usus=User.objects.all()
    pe=Mascota.objects.all()
    
    if request.POST:

        user=request.POST.get("txtEmail","")
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
        usuarion=request.POST.get("txtUsuario")
        try:

            user=User.objects.get(usuario=usuarion)
        except Exception as ex:
            return render(request,'recuperar.html',{'noexiste':True})
        us=user.usuario
        passa=user.passa
        email=user.correo
        
        
        ms='Hola '+us+' gracias pos usar nuestro sistema de recuperacion de usuario su clave es '+passa
        
        fromaddr = 'misperris5@gmail.com'
        toaddrs  = email
        msg = ms
        username = 'misperris5@gmail.com'
        password = 'misperris1998'
        server = smtplib.SMTP('smtp.gmail.com:587')
        server.starttls()
        server.login(username,password)
        server.sendmail(fromaddr, toaddrs,msg)
        server.quit()

        return render(request,'recuperar.html',{'correo':email})
    else:
        return render(request,'recuperar.html')

@login_required
def servicios(request):
    na=request.user.is_staff
    mas=Mascota.objects.all()    
    if na == True:
        if request.POST:           
            return render(request,'core/servicios.html',{'perros':mas,'admin':True})

        else:
            return render(request,'core/servicios.html',{'ingresado':True,'perritos':mas})
    elif na == False:
            return render(request,'core/home.html',{'ingresado':True,'perritos':mas})

def menu(request):
    # return render(request,'core/menu.html')
    mas=Mascota.objects.all()
    na=request.user.is_staff
    if  request.user.is_authenticated:
        na=request.user.is_staff
        if na ==True:
            return render(request,'core/menu.html',{'perritos':mas,'ingresado':True,'na':na,'admin':True})
        else:
            return render(request,'core/menu.html',{'perritos':mas,'ingresado':True,'na':na})
    else:
        return render(request,'core/menu.html',{'perritos':mas,'deslog':True})
@login_required
def menu_perros(request):
    na=request.user.is_staff
    mas=Mascota.objects.all()    
    if na == True:
        if request.POST:           
            return render(request,'core/menu_perros.html',{'perros':mas,'admin':True})

        else:
            return render(request,'core/menu_perros.html',{'ingresado':True,'perritos':mas})
    elif na == False:
            return render(request,'core/home.html',{'ingresado':True,'perritos':mas})

            
def menu_persona(request):
    na=request.user.is_staff
    mas=Mascota.objects.all()    
    if na == True:
        if request.POST:           
            return render(request,'core/menu_persona.html',{'perros':mas,'admin':True})

        else:
            return render(request,'core/menu_persona.html',{'ingresado':True,'perritos':mas})
    elif na == False:
            return render(request,'core/home.html',{'ingresado':True,'perritos':mas})


def galeria(request):
    return render(request, 'core/galeria.html')