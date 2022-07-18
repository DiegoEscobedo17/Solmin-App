from contextlib import nullcontext
from django.db import models

# Create your models here.
class Orden(models.Model):
    Nro_orden = models.IntegerField(primary_key=True, verbose_name='Nro Orden')
    fecha_ingreso = models.DateField(verbose_name='Fecha Ingreso')
    fecha_salida = models.DateField(verbose_name='Fecha Salida')

class Cliente(models.Model):
    id_cliente = models.IntegerField(primary_key=True, verbose_name='Id Clente')
    nombre = models.CharField(max_length=20, verbose_name='Nombre')
    direccion = models.CharField(max_length=20, verbose_name='Direccion')
    RUC = models.IntegerField(verbose_name='RUC')
    DNI = models.CharField(max_length=8, verbose_name='DNI')
    encargado = models.CharField(max_length=20, verbose_name='Encargado')
    telefono = models.IntegerField(verbose_name='Telefono')
    email = models.CharField(max_length=50, verbose_name='Email')
    Nro_orden = models.ForeignKey(Orden, null=True, blank=True, on_delete=models.CASCADE, verbose_name='Nro Orden')

class Soldadora (models.Model):
    id_soldadora = models.IntegerField(primary_key=True, verbose_name='Id Soldadora')
    marca = models.CharField(max_length=50, verbose_name='Marca')
    modelo = models.CharField(max_length=50, verbose_name='Modelo')
    Nro_serie = models.CharField(max_length=40, verbose_name='Nro. Serie')
    code = models.CharField(max_length=40, verbose_name='Code')
    horometro = models.CharField(max_length=40, verbose_name='Horometro')
    diagnostico = models.CharField(max_length=120, verbose_name='Diagnostico')
    foto_ingreso = models.ImageField(upload_to='fotos/', verbose_name='Imagen Ingreso', null=True)
    foto_reparacion = models.ImageField(upload_to='fotos/', verbose_name='Imagen Reparacion', null=True)
    foto_salida = models.ImageField(upload_to='fotos/', verbose_name='Imagen Salida', null=True)
    Nro_orden = models.ForeignKey(Orden, null=True, blank=True, on_delete=models.CASCADE, verbose_name='Nro Orden')

class Encargado (models.Model):
    receptor = models.CharField(primary_key=True, max_length=30, verbose_name='Recepcionado Por')
    servicio = models.CharField(max_length=40, verbose_name='Servicio')
    falla = models.CharField(max_length=100, verbose_name='falla')
    Nro_orden = models.ForeignKey(Orden, null=True, blank=True, on_delete=models.CASCADE, verbose_name='Nro Orden')

class Planchado (models.Model):
    cod_p = models.IntegerField(verbose_name='Cod. Producto')
    cant = models.IntegerField(verbose_name='Cantidad')
    descripcion = models.CharField(max_length=150, verbose_name='Descripcion')
    Nro_orden = models.ForeignKey(Orden, null=True, blank=True, on_delete=models.CASCADE, verbose_name='Nro Orden')

class Elementos (models.Model):
    antorcha = models.BooleanField(verbose_name='Antorcha')
    portaelectrodo = models.BooleanField(verbose_name='Porta Electrodo')
    pinza_masa = models.BooleanField(verbose_name='Pinza Masa')
    cable_acometida = models.BooleanField(verbose_name='Cable Acometida')
    clavija = models.BooleanField(verbose_name='Clavija')
    regulador_gas = models.BooleanField(verbose_name='Regulador de Gas')
    manguera_gas = models.BooleanField(verbose_name='Manguera de Gas')
    pernos = models.BooleanField(verbose_name='Pernos')
    ridillos = models.BooleanField(verbose_name='Ridillos')
    perillas = models.BooleanField(verbose_name='Perillas')
    asas = models.BooleanField(verbose_name='Asas')
    bases_ruedas = models.BooleanField(verbose_name='Base de Ruedas')
    carrete = models.BooleanField(verbose_name='Carrete')
    consumibles = models.BooleanField(verbose_name='Consumibles')
    chupon_o_conductor = models.BooleanField(verbose_name='Chupón o Conductor')
    otros = models.BooleanField(verbose_name='Otros')
    Nro_orden = models.ForeignKey(Orden, null=True, blank=True, on_delete=models.CASCADE, verbose_name='Nro Orden')
    id_cliente = models.ForeignKey(Cliente, null=True, blank=True, on_delete=models.CASCADE, verbose_name='Id Cliente')
    id_soldadora = models.ForeignKey(Soldadora, null=True, blank=True, on_delete=models.CASCADE, verbose_name='Id Soldadora')