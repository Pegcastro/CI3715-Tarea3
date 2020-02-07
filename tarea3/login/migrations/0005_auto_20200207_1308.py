# Generated by Django 3.0.3 on 2020-02-07 17:08

from django.db import migrations, models
import login.validators


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0004_auto_20200205_1722'),
    ]

    operations = [
        migrations.AlterField(
            model_name='seguridad',
            name='email',
            field=models.CharField(max_length=120, validators=[login.validators.validate_correct_email]),
        ),
        migrations.AlterField(
            model_name='seguridad',
            name='password',
            field=models.CharField(max_length=16, validators=[login.validators.validate_correct_password]),
        ),
    ]
