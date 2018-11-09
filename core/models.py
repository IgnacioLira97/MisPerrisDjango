from django.db import models
import datetime

# Create your models here.
class Estado(models.Model):
    idEstado=models.IntegerField(primary_key=True)
    name=models.CharField(max_length=30)

    def __str__(self):
        return self.name

class Region(models.Model):
    idRegion=models.IntegerField(primary_key=True)
    name=models.CharField(max_length=100)
    
    def __str__(self):
        return self.name

class Ciudad(models.Model):
    idCiudad=models.IntegerField(primary_key=True)
    name=models.CharField(max_length=100)
    idRegion=models.ForeignKey(Region,on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name


class tipoVivienda(models.Model):
    idTipo=models.IntegerField(primary_key=True)
    tipo=models.CharField(max_length=20)

    def __str__(self):
        return self.tipo

class Raza(models.Model):
    idRaza=models.IntegerField(primary_key=True)
    Raza=models.CharField(max_length=60)

    def __str__(self):
        return self.Raza

class Usuario(models.Model):
    run=models.CharField(max_length=14,primary_key=True)
    usuario=models.CharField(max_length=30)
    nombre=models.CharField(max_length=255, null=True)
    correo=models.CharField(max_length=50)
    fechaNacimiento=models.DateField()
    telefono=models.CharField(max_length=9)
    password=models.CharField(max_length=100)
    region=models.CharField(max_length=150)
    ciudad=models.CharField(max_length=150)
    tipoVivienda=models.ForeignKey(tipoVivienda,on_delete=models.CASCADE)

    def __str__(self):
        return self.run

class Mascota(models.Model):
    idMascota=models.IntegerField(primary_key=True)
    name=models.CharField(max_length=50)
    foto=models.FileField(upload_to='media')
    descripcion=models.CharField(max_length=255)
    raza=models.ForeignKey(Raza,on_delete=models.CASCADE)
    idEstado=models.ForeignKey(Estado,on_delete=models.CASCADE)

    def __str__(self):
        return self.name

