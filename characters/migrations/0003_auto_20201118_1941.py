# Generated by Django 3.1.2 on 2020-11-18 19:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('characters', '0002_charpictures'),
    ]

    operations = [
        migrations.AlterField(
            model_name='charpictures',
            name='character',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='characters.characters'),
        ),
    ]
