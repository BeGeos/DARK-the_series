# Generated by Django 3.1.2 on 2020-11-18 20:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('characters', '0003_auto_20201118_1941'),
    ]

    operations = [
        migrations.AlterField(
            model_name='charpictures',
            name='image',
            field=models.ImageField(upload_to='media'),
        ),
    ]
