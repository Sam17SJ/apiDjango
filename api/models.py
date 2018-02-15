from django.db import models
from django.contrib.auth.models import User
# para la aplicacion de cuentas
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
from django.contrib.postgres.fields import ArrayField
# termina para aplicacion de cuentas
@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)

# Create your models here.
class Estrella(models.Model):
	"""docstring for Estrella"""
	rankin= models.IntegerField()
	def __str__(self):
		return str(self.rankin)
		
# class Imagen(models.Model):
# 	"""docstring for Imagenes"""
# 	alto= models.IntegerField()
# 	ancho= models.IntegerField()
# 	def __init__(self, arg):
# 		super (Imagenes, self).__init__()
# 		self.arg = arg

class UsuarioGratuito(models.Model):
	"""docstring for UsuarioGratuito"""
	nombre= models.CharField(max_length=25)
	numTelefonico = models.IntegerField()
	idUser = models.ForeignKey(User)
	def __str__(self):
		return str(self.nombre)
		

class Broker(models.Model):
	"""docstring for Broker"""
	nombre= models.CharField(max_length=25)
	estrella = models.ForeignKey(Estrella)
	descripcion = models.CharField(max_length=250)
	numTelefonico = models.IntegerField()
	def __str__(self):
		return str(self.nombre)
		

# class Corporacion(models.Model):
# 	nombre= models.CharField(max_length=25)
# 	estrella = models.ForeignKey(Estrella)
# 	descripcion = models.CharField(max_length=250)
# 	numTelefonico = models.IntegerField()
# 	"""docstring for Corporacion"""
# 	def __init__(self, arg):
# 		super(Corporacion, self).__init__()
# 		self.arg = arg
		

# def user_directory_path(instance, filename):
#     # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
#     return 'uploads/user_{0}/{1}'.format(instance.id, filename)

class Propiedad(models.Model):
	titulo = models.CharField(max_length=35)
	# descripcio= models.CharField(max_length=250, blank=True)
# 	ubicacion = models.ForeignKey(Ubicacion)
	precio = models.FloatField()
	# propietario = models.ForeignKey(UsuarioGratuito, blank=True)
	imagen = ArrayField(models.CharField(max_length=250, blank=True),size=10)
	def __str__(self):
		return str(self.titulo)

class Image(models.Model):
	img = models.ImageField(upload_to='uploads/{0}'.format("%d-%m-%y/%H_%M_%S"), default='uploads/f1.png')
	def __str__(self):
		return str(self.img)



class Contrato(models.Model):
	estado = models.IntegerField()
	fechaInicio= models.DateField()
	acuerdo = models.IntegerField()
	broker = models.OneToOneField(Broker)
	propiedad = models.OneToOneField(Propiedad)
	"""docstring for Contrato"""
	def __str__(self):
		return str(self.acuerdo)
		