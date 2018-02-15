from django.db import models
from django.contrib.auth.models import User

# Create your models here.
# class Estrella(models.Model):
# 	"""docstring for Estrella"""
# 	rankin= models.IntegerField()
# 	def __str__(self):
# 		return str(self.rankin)
		
# class Imagen(models.Model):
# 	"""docstring for Imagenes"""
# 	alto= models.IntegerField()
# 	ancho= models.IntegerField()
# 	def __init__(self, arg):
# 		super (Imagenes, self).__init__()
# 		self.arg = arg

# class UsuarioGratuito(models.Model):
# 	"""docstring for UsuarioGratuito"""
# 	nombre= models.CharField(max_length=25)
# 	numTelefonico = models.IntegerField()
# 	idUser = models.ForeignKey(User)
# 	def __init__(self, arg):
# 		super(UsuarioGratuito, self).__init__()
# 		self.arg = arg

# class Broker(models.Model):
# 	"""docstring for Broker"""
# 	nombre= models.CharField(max_length=25)
# 	estrella = models.ForeignKey(Estrella)
# 	descripcion = models.CharField(max_length=250)
# 	numTelefonico = models.IntegerField()
# 	def __init__(self, arg):
# 		super(Broker, self).__init__()
# 		self.arg = arg

# class Corporacion(models.Model):
# 	nombre= models.CharField(max_length=25)
# 	estrella = models.ForeignKey(Estrella)
# 	descripcion = models.CharField(max_length=250)
# 	numTelefonico = models.IntegerField()
# 	"""docstring for Corporacion"""
# 	def __init__(self, arg):
# 		super(Corporacion, self).__init__()
# 		self.arg = arg
		
# class Propiedad(models.Model):
# 	titulo = models.CharField(max_length=35)
# 	descripcio= models.CharField(max_length=250)
# 	ubicacion = models.ForeignKey(Ubicacion)
# 	precio = models.FloatField()
# 	propietario = models.ForeignKey(UsuarioGratuito)
# 	"""docstring for Propiedad"""
# 	def __init__(self, arg):
# 		super(Propiedad, self).__init__()
# 		self.arg = arg

# class Contrato(models.Model):
# 	estado = models.IntegerField()
# 	fechaInicio= models.DateField()
# 	acuerdo = models.IntegerField()
# 	broker = models.OneToOneField(Broker)
# 	propiedad = models.OneToOneField(Propiedad)
# 	"""docstring for Contrato"""
# 	def __init__(self, arg):
# 		super(Contrato, self).__init__()
# 		self.arg = arg
# 				