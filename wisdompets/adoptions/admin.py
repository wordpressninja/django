from django.contrib import admin
from .models import Pet

# Add the admin model for app
@admin.register(Pet)
class PetAdmin(admin.ModelAdmin):
    list_display = ['name', 'species', 'breed', 'age', 'sex']
