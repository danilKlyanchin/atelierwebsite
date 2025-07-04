from django.contrib import admin
from .models import AtelierEntity


class AtelierEntityAdmin(admin.ModelAdmin):
    pass


admin.site.register(AtelierEntity, AtelierEntityAdmin)
