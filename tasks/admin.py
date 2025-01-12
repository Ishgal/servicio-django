from django.contrib import admin
from .models import task
# Register your models here.

class TaskAdmin(admin.ModelAdmin):
    readonly_fields = ("Creado",)

admin.site.register(task,TaskAdmin)