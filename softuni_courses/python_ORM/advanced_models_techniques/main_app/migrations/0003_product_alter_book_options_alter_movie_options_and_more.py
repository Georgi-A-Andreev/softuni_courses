# Generated by Django 4.2.4 on 2023-11-10 12:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_book_movie_music_alter_customer_email_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
        migrations.AlterModelOptions(
            name='book',
            options={'ordering': ['-created_at', 'title'], 'verbose_name': 'Model Book', 'verbose_name_plural': 'Models of type - Book'},
        ),
        migrations.AlterModelOptions(
            name='movie',
            options={'ordering': ['-created_at', 'title'], 'verbose_name': 'Model Movie', 'verbose_name_plural': 'Models of type - Movie'},
        ),
        migrations.AlterModelOptions(
            name='music',
            options={'ordering': ['-created_at', 'title'], 'verbose_name': 'Model Music', 'verbose_name_plural': 'Models of type - Music'},
        ),
        migrations.CreateModel(
            name='DiscountedProduct',
            fields=[
            ],
            options={
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('main_app.product',),
        ),
    ]
