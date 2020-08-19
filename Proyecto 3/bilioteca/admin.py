from django.contrib import admin
from .models import *

class MaterialInline(admin.TabularInline):
    model = Material
    extra = 0
    fields = ['tipoMaterial','autor','titulo','anio','status']

class PersonaInline(admin.TabularInline):
    model = Persona
    fields = ['tipoPersona','nombre','apellido','correo','telefono','numLibros','adeudo']

class PrestamoAdmin(admin.ModelAdmin):
    list_display = ['codigo','fechaSalida','fechaRegreso',]
    list_display_links = ['codigo','fechaSalida','fechaRegreso',]
    search_fields = ['codigo','fechaSalida','fechaRegreso',]
    inlines = [MaterialInline, PersonaInline]

class LibroAdmin(admin.ModelAdmin):
    list_display = ['tipoMaterial','codigo','autor','titulo','anio','status','editorial',]
    list_display_links = ['tipoMaterial','codigo','autor','titulo','anio','status','editorial',]
    search_fields = ['tipoMaterial','codigo','autor','titulo','anio','status','editorial',]
    fieldsets = (
        ("Descripcion", {
            'fields':('tipoMaterial','titulo','anio','status','editorial','portada',)
        }),
        ('Autor', {
            'fields':('autor',)
        }),
    )
class RevistaAdmin(admin.ModelAdmin):
    list_display = ['tipoMaterial','codigo','autor','titulo','anio','status',]
    list_display_links = ['tipoMaterial','codigo','autor','titulo','anio','status',]
    search_fields = ['tipoMaterial','codigo','autor','titulo','anio','status',]
    fieldsets = (
        ("Descripcion", {
            'fields':('tipoMaterial','titulo','anio','status',)
        }),
        ('Autor', {
            'fields':('autor',)
        }),
    )

class AlumnoAdmin(admin.ModelAdmin):
    list_display = ['tipoPersona','nombre','apellido','correo','telefono','numLibros','adeudo','matricula',]
    list_display_links = ['matricula',]
    search_fields = ['matricula',]
    fieldsets = (
        ("Descripcion", {
            'fields':('tipoPersona', 'nombre', 'apellido', 'numLibros', 'adeudo',)
        }),
        ('Contacto', {
            'fields':('correo', 'telefono',)
        }),
    )

class ProfesorAdmin(admin.ModelAdmin):
    list_display = ['tipoPersona','nombre','apellido','correo','telefono','numLibros','adeudo','numEmpleado',]
    list_display_links = ['numEmpleado',]
    search_fields = ['numEmpleado',]
    fieldsets = (
        ("Descripcion", {
            'fields':('tipoPersona', 'nombre', 'apellido', 'numLibros', 'adeudo',)
        }),
        ('Contacto', {
            'fields':('correo', 'telefono',)
        }),
    )

class MaterialAdmin(admin.ModelAdmin):
    list_display = ['tipoMaterial','codigo','autor','titulo','anio','status',]
    list_display_links = ['tipoMaterial','codigo','autor','titulo','anio','status',]
    search_fields = ['tipoMaterial','codigo','autor','titulo','anio','status',]

class PersonaAdmin(admin.ModelAdmin):
    list_display = ['tipoPersona','nombre','apellido','correo','telefono','numLibros','adeudo',]
    list_display_links = ['tipoPersona','nombre','apellido','correo','telefono','numLibros','adeudo',]
    search_fields = ['tipoPersona','nombre','apellido','correo','telefono','numLibros','adeudo',]



# Register your models here.

admin.site.register(Prestamo, PrestamoAdmin)
admin.site.register(Persona, PersonaAdmin)
admin.site.register(Profesor, ProfesorAdmin)
admin.site.register(Alumno, AlumnoAdmin)
admin.site.register(Material, MaterialAdmin)
admin.site.register(Libro, LibroAdmin)
admin.site.register(Revista, RevistaAdmin)