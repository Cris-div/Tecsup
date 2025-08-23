from django.contrib import admin
from .models import Item

# Registrar el modelo Item en el admin
admin.site.register(Item)
