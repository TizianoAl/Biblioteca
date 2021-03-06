from django.db import models

# Create your models here.

class Prestamo(models.Model):
    codigo = models.AutoField(primary_key=True)
    fechaSalida = models.CharField(max_length=143)
    fechaRegreso = models.CharField(max_length=143)

    def cuota():
        pass

    def __str__(self):
        return str(self.codigo)

class Material(models.Model):
    codigo = models.AutoField(primary_key=True)
    tipoMaterial = models.CharField(max_length=143)
    autor = models.CharField(max_length=100)
    titulo = models.CharField(max_length=243)
    anio = models.IntegerField()
    status = models.CharField(max_length=143)
    prestamo = models.ForeignKey('Prestamo', on_delete=models.CASCADE, null=False)

    def altaMaterial():
        pass   

    def bajaMaterial():
        pass  

    def cambioMaterial():
        pass 

    def __str__(self):
        return str(self.titulo)

class Persona(models.Model):
    tipoPersona = models.CharField(max_length=143)
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=143)
    correo = models.CharField(max_length=243)
    telefono = models.IntegerField()
    numLibros = models.IntegerField()
    adeudo = models.FloatField()
    prestamo = models.OneToOneField('Prestamo', on_delete=models.CASCADE, null=False)

    def llevarMaterial():
        pass   

    def dejarMaterial():
        pass  

    def __str__(self):
        return str(self.nombre)

class Libro(Material):
    editorial = models.CharField(max_length=143)
    portada = models.FileField(blank = True)

    def __str__(self):
        return str(self.titulo)

class Revista(Material):

    def __str__(self):
        return str(self.titulo)

class Alumno(Persona):
    matricula = models.AutoField(primary_key=True)

    def __str__(self):
        return str(self.nombre)

class Profesor(Persona):
    numEmpleado = models.AutoField(primary_key=True)

    def __str__(self):
        return str(self.nombre)




