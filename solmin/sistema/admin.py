from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(Orden)
admin.site.register(Cliente)
admin.site.register(Soldadora)
admin.site.register(Encargado)
admin.site.register(Elementos)
admin.site.register(Planchado)


