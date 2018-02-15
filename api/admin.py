from django.contrib import admin

# Register your models here.

from .models import *

admin.site.register(Estrella)
admin.site.register(Propiedad)
admin.site.register(Broker)
admin.site.register(UsuarioGratuito)
admin.site.register(Image)
admin.site.register(Contrato)
