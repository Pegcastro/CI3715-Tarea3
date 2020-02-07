from .validators import *
from django.core.exceptions import ValidationError

def registrarUsuario(email, password, password2):
    try:
        validate_correct_email(email)
        validate_correct_password(password)
        validate_same_password(password1, password2)
    except ValidationError:
        return False, ValidationError
    return True, email

def ingresarUsuario(email, password):
    try:
        validate_correct_email(email)
        validate_correct_password(password)
    except ValidationError:
        return False, ValidationError
    return True, email
