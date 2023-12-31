# Generated by Django 4.2.4 on 2023-10-18 09:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Spaces', '0010_delete_rating_alter_comment_id_alter_comment_rating'),
    ]

    operations = [
        migrations.CreateModel(
            name='Damage',
            fields=[
                ('id', models.AutoField(editable=False, primary_key=True, serialize=False, unique=True)),
                ('space_name', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('image', models.ImageField(upload_to='damages/images')),
                ('date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
