# Generated by Django 4.2.4 on 2023-08-10 20:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('admins', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='OcuppiedSpaces',
            fields=[
                ('id', models.AutoField(editable=False, primary_key=True, serialize=False, unique=True)),
                ('occupied_at', models.DateTimeField(auto_now_add=True)),
                ('unoccupied_at', models.DateTimeField(auto_now=True)),
                ('space_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='admins.spaces')),
            ],
        ),
    ]