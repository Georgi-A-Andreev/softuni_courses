# Generated by Django 4.2.4 on 2023-11-18 16:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_alter_movie_director_alter_movie_starring_actor'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='actors',
            field=models.ManyToManyField(related_name='movies_many', to='main_app.actor'),
        ),
        migrations.AlterField(
            model_name='movie',
            name='director',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='movies', to='main_app.director'),
        ),
        migrations.AlterField(
            model_name='movie',
            name='starring_actor',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='movies', to='main_app.actor'),
        ),
    ]
