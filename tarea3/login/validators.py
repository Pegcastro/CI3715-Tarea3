import re
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

regexEmail = '^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$'
regexPass = ''

def validate_correct_password(value):
    pass
    # if value % 2 != 0:
    #     raise ValidationError(
    #         _('%(value)s is not an even number'),
    #         params={'value': value},
    #     )

def validate_correct_email(value):
    match = re.search(self.regex, email)
        if(not match):
            raise ValidationError(
            _('%(value)s is not a valid email'),
            params={'value': value},
            )

    # try:
    #     RegexValidator(regex=r'^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$')
    # except:
    #     raise ValidationError(
    #         _('%(value)s is not a valid email'),
    #         params={'value': value},
    #     )