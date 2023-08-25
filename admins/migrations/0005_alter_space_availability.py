# Generated by Django 4.2.4 on 2023-08-13 10:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admins', '0004_alter_space_availability'),
    ]

    operations = [
        migrations.AlterField(
            model_name='space',
            name='availability',
            field=models.IntegerField(choices=[(0, 'Disponible'), (1, 'Ocupado'), (2, 'Deshabilitado')]),
        ),
    ]