from django.db import models
from django.core.validators import RegexValidator, MinLengthValidator
from .validators import validate_correct_password

# Create your models here.
class Seguridad(models.Model):
    email = models.CharField(max_length=120, validators=[RegexValidator(regex=r'^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$')])
    password = models.CharField(max_length=16, validators=[MinLengthValidator(8), validate_correct_password])

    def __str__(self):
        return self.email + ': ' + self.password[::-1]

    
