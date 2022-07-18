from unicodedata import name
from django.urls import path
from . import views

urlpatterns = [
    path('',views.inicio, name='inicio'),
    path('nosotros',views.nosotros, name='nosotros'),
    
    path('ordenes',views.ordenes, name='ordenes'),
    path('ordenes/crear',views.crear_orden, name='crearorden'),
    path('ordenes/editar',views.editar_orden, name='editarorden'),
    path('eliminar/<int:Nro_orden>',views.eliminar_orden,name='eliminarorden'),
    path('ordenes/editar/<int:Nro_orden>',views.editar_orden, name="editarorden"),

    path('clientes',views.clientes, name='clientes'),
    
    path('soldadoras',views.soldadoras, name='soldadoras'),
    
    path('elementos',views.elementos, name='elementos'),
    
    path('encargados',views.encargados, name='encargados'),
    
    path('planchados',views.planchados, name='planchados'),
]