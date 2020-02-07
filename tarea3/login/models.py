from django.db import models
from django.core.validators import RegexValidator, MinLengthValidator
from .validators import validate_correct_password, validate_correct_email

# Create your models here.
class Seguridad(models.Model):
    email = models.CharField(max_length=120, validators=[validate_correct_email])
    password = models.CharField(max_length=16, validators=[validate_correct_password])

    def __str__(self):
        return self.email + ': ' + self.password[::-1]