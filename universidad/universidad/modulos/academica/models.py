from django.db import models

# Create your models here.

class Carrera(models.Model):
    codigo = models.CharField(max_length=3, primary_key=True)
    nombre =  models.CharField(max_length=50)
    duracion = models.PositiveSmallIntegerField(default=5)

    def __str__(self):
        txt = "{0} (Duración : {1} año(s))"
        return txt.format(self.nombre, self.duracion)

class Estudiante(models.Model):
    carnet = models.CharField(max_length=8,primary_key=True)
    apellido_paterno = models.CharField(max_length=35)
    apellido_materno = models.CharField(max_length=35)
    nombres = models.CharField(max_length=35)
    fecha_nacimiento= models.DateField()
    sexos = [
        ('F','Femenino'),
        ('M', 'Masculino')
    ]
    sexo = models.CharField(max_length=1,choices=sexos, default='F')
    carrera = models.ForeignKey(Carrera, null=False, blank=False, on_delete=models.CASCADE)
    vigencia = models.BooleanField(default=True)

    def nombreCompleto(self):
        txt = "{0} {1}, {2}"
        return txt.format(self.apellido_paterno,self.apellido_materno,self.nombres)
    
    def __str__(self):
        txt = "{0} / Carrera : {1} / {2}"
        if self.vigencia:
            estado_estudiante = "Vigente"
        else:
            estado_estudiante = "Dado de Baja"

        return txt.format(self.nombreCompleto(),self.carrera, estado_estudiante)

class Curso(models.Model):
    codigo = models.CharField(max_length=6, primary_key=True)
    nombre = models.CharField(max_length=30)
    creditos = models.PositiveSmallIntegerField()
    docente = models.CharField(max_length=100)

    def __str__(self):
        txt = "{0} ({1}) / Docente : {2}"
        return txt.format(self.nombre, self.codigo, self.docente)

class Matricula(models.Model):
    id = models.AutoField(primary_key=True)
    estudiante = models.ForeignKey(Estudiante, null=False, blank=False, on_delete=models.CASCADE)
    curso = models.ForeignKey(Curso, null=False, blank=False, on_delete=models.CASCADE)
    fechaMatricula = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        txt = "{0} matriculad{1} en el curso {2} / Fecha : {3}"
        if self.estudiante.sexo == "F":
            letrasexo="a"
        else:
            letrasexo = "o"
        
        fechaMat = self.fechaMatricula.strftime("%A %d/%m/%Y %H:%M:%S")
        return txt.format(self.estudiante.nombreCompleto(),letrasexo,self.curso, fechaMat)