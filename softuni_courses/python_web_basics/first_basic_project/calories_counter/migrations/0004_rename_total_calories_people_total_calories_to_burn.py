# Generated by Django 5.0 on 2023-12-15 20:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('calories_counter', '0003_rename_activity_activities'),
    ]

    operations = [
        migrations.RenameField(
            model_name='people',
            old_name='total_calories',
            new_name='total_calories_to_burn',
        ),
    ]
