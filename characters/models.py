from django.db import models


# Create your models here.
class Characters(models.Model):
    sex = (
        ('M', 'Male'),
        ('F', 'Female')
    )
    fullname = models.CharField(max_length=50)
    father = models.CharField(max_length=50, blank=True)
    mother = models.CharField(max_length=50, blank=True)
    date_of_birth = models.IntegerField()
    status = models.BooleanField()
    description = models.TextField()
    gender = models.CharField(max_length=1, choices=sex)


class CharPictures(models.Model):
    image = models.ImageField(upload_to='static/images')
    character = models.ForeignKey(Characters, on_delete=models.CASCADE, blank=True, null=True)
