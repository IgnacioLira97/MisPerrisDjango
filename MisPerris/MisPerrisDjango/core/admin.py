from django.contrib import admin

# Register your models here.

from .models import Estado, Region, Ciudad, tipoVivienda, Raza, User, Mascota

    
admin.site.register(Estado)
admin.site.register(Region)
admin.site.register(Ciudad)
admin.site.register(tipoVivienda)
admin.site.register(Raza)
admin.site.register(User)
admin.site.register(Mascota)

# admin.site.register(Estado)
# admin.site.register(Raza)
# admin.site.register(Mascota)
# admin.site.register(Region)
# admin.site.register(Ciudad)
# admin.site.register(Vivienda)
# admin.site.register(TipoUser)
# admin.site.register(Persona)

