# Generated by Django 4.2.4 on 2023-11-23 17:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='actors',
            field=models.ManyToManyField(related_name='movies_actors', to='main_app.actor'),
        ),
    ]
