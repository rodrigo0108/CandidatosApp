from django.db import models
from datetime import date

# Create your models here.
class Candidato(models.Model):
    nombres = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=100)
    fecha_nac = models.DateField('Fecha de nacimiento',default=date.today)
    fecha_in_polt = models.DateField('Fecha de inicio en la política', default=date.today)

    #Es importante añadir los métodos __str__() a sus modelos, para representaciones de objetos se usan en todo el sitio administrativo generado automáticamente de Django.
    def __str__(self):
        return self.nombres + " " + self.apellidos
