from django.contrib import admin

# Register your models here.

from .models import Estado, Region, Ciudad, tipoVivienda, Raza, Usuario, Mascota

    
admin.site.register(Estado)
admin.site.register(Region)
admin.site.register(Ciudad)
admin.site.register(tipoVivienda)
admin.site.register(Raza)
admin.site.register(Usuario)
admin.site.register(Mascota)


