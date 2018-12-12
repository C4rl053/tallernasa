from django.db import models

# Create your models here.
class Marca(models.Model):
	nombre		= models.CharField(max_length = 100)
	def __str__ (self):
		return self.nombre

class Modelo(models.Model):
	nombre		= models.CharField(max_length = 100)
	marca       = models.ForeignKey(Marca, on_delete=models.CASCADE)
	def __str__ (self):
		return self.nombre

class Catalogo(models.Model):
	nombre		= models.CharField(max_length = 100)
	descripcion	= models.CharField(max_length = 500)
	modelo      = models.ManyToManyField(Modelo, null = True, blank = True)	
	def __str__ (self):
		return self.nombre

class Accesorio(models.Model):
	nombre		= models.CharField(max_length = 100)
	descripcion	= models.CharField(max_length = 500)
	status		= models.BooleanField(default = True)
	precio 		= models.DecimalField(max_digits = 6, decimal_places = 2)
	stock		= models.IntegerField()
	catalogo    = models.ForeignKey(Catalogo, on_delete=models.CASCADE)	
	imagen      = models.ImageField(upload_to='fotos',blank=True,null=True)
	marca   	= models.ForeignKey(Marca, on_delete=models.CASCADE)
	def __str__ (self):
		return self.nombre

class Repuesto(models.Model):
	nombre		= models.CharField(max_length = 100)
	descripcion	= models.CharField(max_length = 500)
	status		= models.BooleanField(default = True)
	precio 		= models.DecimalField(max_digits = 6, decimal_places = 2)
	stock		= models.IntegerField()
	catalogo    = models.ManyToManyField(Catalogo, null = True, blank = True)
	imagen      = models.ImageField(upload_to='fotos',blank=True,null=True)
	marca   	= models.ForeignKey(Marca, on_delete=models.CASCADE)
	def __str__ (self):
		return self.nombre

