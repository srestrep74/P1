# Generated by Django 4.2.4 on 2023-09-07 17:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Admins', '0004_space_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='space',
            name='image',
            field=models.ImageField(default='piscina.png', upload_to='spaces/images'),
        ),
    ]
