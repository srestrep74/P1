# Generated by Django 4.2.4 on 2023-09-09 18:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Admins', '0009_space_occupancy_alter_space_latitude_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='space',
            name='max_occupancy',
            field=models.IntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='space',
            name='occupancy',
            field=models.IntegerField(default=0),
        ),
    ]
