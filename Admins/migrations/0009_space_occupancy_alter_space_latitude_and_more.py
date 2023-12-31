# Generated by Django 4.2.4 on 2023-09-09 17:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Admins', '0008_alter_space_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='space',
            name='occupancy',
            field=models.IntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='space',
            name='latitude',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='space',
            name='longitude',
            field=models.FloatField(default=0),
        ),
    ]
