from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from apps.parametros.models import Sucursal

class UserManager(BaseUserManager, models.Manager):

	def _create_user(self, username, email, password, is_staff, is_superuser, **extra_fields):
		
		email = self.normalize_email(email)
		if not email:
			raise ValueError('Email obligatorio')
		
		usermodel = self.model(username = username, email = email, is_active = True, is_staff = is_staff, is_superuser = is_superuser, **extra_fields)
		usermodel.set_password(password)
		usermodel.save( using = self._db)
		return usermodel

	def create_user(self, username, email, password=None, **extra_fields):
		return self._create_user(username, email, password, False, False, **extra_fields)

	def create_superuser(self, username, email, password=None, **extra_fields):
		return self._create_user(username, email, password, True, True, **extra_fields)

class User(AbstractBaseUser, PermissionsMixin):
 	username = models.CharField('Usuario', max_length=25, unique=True)
 	email = models.EmailField('e-mail')
 	first_name = models.CharField('Primer Nombre', max_length=20)
 	last_name = models.CharField('Segundo Nombre', max_length=20)
 	sucursal = models.ForeignKey(Sucursal,  null=True, blank=True)
 	telefono = models.CharField('Teléfono', max_length=15)
 	celular = models.CharField('Celular', max_length=15)
 	picture_user = models.ImageField(upload_to = "usuarios")

 	objects = UserManager()

 	is_active = models.BooleanField('Status del Registro', default = True)
 	is_staff = models.BooleanField('Tipo de Usuario', default = False)

 	USERNAME_FIELD = 'username'
 	REQUIRED_FIELDS = ['email']

 	def get_short_name(self):
 		return self.username