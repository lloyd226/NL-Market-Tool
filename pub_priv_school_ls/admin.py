from django.contrib import admin

# Register your models here.
from .models import School

class SchoolAdmin(admin.ModelAdmin):
    list_display = ["school_name","distance"]
    search_fields=["school_name"]

admin.site.register(School, SchoolAdmin)