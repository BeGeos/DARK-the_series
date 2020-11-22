# Generated by Django 3.1.2 on 2020-11-18 19:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('characters', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CharPictures',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='static/images')),
                ('character', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='characters.characters')),
            ],
        ),
    ]