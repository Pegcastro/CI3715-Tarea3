from .validators import *
from django.core.exceptions import ValidationError
from .models import Seguridad

def registrarUsuario(email, password, password2):
    try:
        validate_correct_email(email)
        validate_correct_password(password)
        validate_same_password(password, password2)
        s = Seguridad()
        s.email = email
        s.password = password2[::-1]
        s.save()
    except ValidationError as err:
        return False, err
    return True, email

def ingresarUsuario(email, password):
    try:
        validate_correct_email(email)
        validate_correct_password(password)
        s = Seguridad.objects.get(email=email)
        assert s.password[::-1] == password
    except ValidationError as err:
        return False, err
    except Seguridad.DoesNotExist as err:
        return False, err
    except AssertionError as err:
        return False, err
    else:
        return True, s.email
