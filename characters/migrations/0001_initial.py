# Generated by Django 3.1.2 on 2020-11-09 19:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Characters',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullname', models.CharField(max_length=50)),
                ('father', models.CharField(blank=True, max_length=50)),
                ('mother', models.CharField(blank=True, max_length=50)),
                ('date_of_birth', models.IntegerField()),
                ('status', models.BooleanField()),
                ('description', models.TextField()),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female')], max_length=1)),
            ],
        ),
    ]
