from django.contrib import admin
from .models import Person, TipoDocumento, Ciudad

# Register your models here.

admin.site.register(TipoDocumento)
admin.site.register(Ciudad)
admin.site.register(Person)