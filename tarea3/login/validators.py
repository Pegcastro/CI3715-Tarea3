import re
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

regexEmail = '^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$'
regexPass = '''[0-9]*[a-z]+[0-9]*[a-z]+[0-9]*[A-Z]+[0-9]+|[0-9]*[a-z]+[0-9]*[A-Z]+[0-9]*[a-z]+[0-9]+|[0-9]*[A-Z]+[0-9]*[a-z]+[0-9]*[a-z]+[0-9]+|[0-9]*[A-Z]+[0-9]*[A-Z]+[0-9]*[a-z]+[0-9]+|[0-9]*[A-Z]+[0-9]*[a-z]+[0-9]*[A-Z]+[0-9]+|[0-9]*[a-z]+[0-9]*[A-Z]+[0-9]*[A-Z]+[0-9]+|[0-9]+[a-z]+[0-9]*[a-z]+[0-9]*[A-Z]+[0-9]*|[0-9]+[a-z]+[0-9]*[A-Z]+[0-9]*[a-z]+[0-9]*|[0-9]+[A-Z]+[0-9]*[a-z]+[0-9]*[a-z]+[0-9]*|[0-9]+[A-Z]+[0-9]*[A-Z]+[0-9]*[a-z]+[0-9]*|[0-9]+[A-Z]+[0-9]*[a-z]+[0-9]*[A-Z]+[0-9]*|[0-9]+[a-z]+[0-9]*[A-Z]+[0-9]*[A-Z]+[0-9]*|[0-9]*[a-z]+[0-9]+[a-z]+[0-9]*[A-Z]+[0-9]*|[0-9]*[a-z]+[0-9]+[A-Z]+[0-9]*[a-z]+[0-9]*|[0-9]*[A-Z]+[0-9]+[a-z]+[0-9]*[a-z]+[0-9]*|[0-9]*[A-Z]+[0-9]+[A-Z]+[0-9]*[a-z]+[0-9]*|[0-9]*[A-Z]+[0-9]+[a-z]+[0-9]*[A-Z]+[0-9]*|[0-9]*[a-z]+[0-9]+[A-Z]+[0-9]*[A-Z]+[0-9]*|[0-9]*[a-z]+[0-9]*[a-z]+[0-9]+[A-Z]+[0-9]*|[0-9]*[a-z]+[0-9]*[A-Z]+[0-9]+[a-z]+[0-9]*|[0-9]*[A-Z]+[0-9]*[a-z]+[0-9]+[a-z]+[0-9]*|[0-9]*[A-Z]+[0-9]*[A-Z]+[0-9]+[a-z]+[0-9]*|[0-9]*[A-Z]+[0-9]*[a-z]+[0-9]+[A-Z]+[0-9]*|[0-9]*[a-z]+[0-9]*[A-Z]+[0-9]+[A-Z]+[0-9]*'''

def validate_correct_password(value):
    match = re.search(regexPass, value)
    if(not match or not (8 >= len(value) <= 16)):
        raise ValidationError(
        _('%(value)s is not a valid password'),
        params={'value': value},
        )

def validate_correct_email(value):
    match = re.search(regexEmail, value)
    if(not match):
        raise ValidationError(
        _('%(value)s is not a valid email'),
        params={'value': value},
        )

def validate_same_password(value1, value2):
    match = (value1 == value2)
    if(not match):
        raise ValidationError(
        _('%(value1)s and %(value2)s do not match'),
        params={'value1': value1,
                'value2': value2},
        )