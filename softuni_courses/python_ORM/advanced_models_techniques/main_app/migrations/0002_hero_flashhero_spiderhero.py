# Generated by Django 4.2.4 on 2023-11-10 13:26

from django.db import migrations, models
import main_app.mixins


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Hero',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('hero_title', models.CharField(max_length=100)),
                ('energy', models.PositiveIntegerField()),
            ],
            bases=(models.Model, main_app.mixins.RechargeEnergyMixin),
        ),
        migrations.CreateModel(
            name='FlashHero',
            fields=[
            ],
            options={
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('main_app.hero',),
        ),
        migrations.CreateModel(
            name='SpiderHero',
            fields=[
            ],
            options={
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('main_app.hero',),
        ),
    ]
