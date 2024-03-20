from django.db import models

# Create your models here.
class Book(models.Model):
  GENRES=[
     ('action', 'Action'),
        ('romance', 'Romance'),
        ('sci-fi', 'Sci-fi'),
        ('religion', 'Religion'),
  ]
  title = models.CharField(max_length=200)
  author = models.CharField(max_length=200)
  genre = models.CharField(max_length=20, choices=GENRES,default="")
  price = models.DecimalField(max_digits=5,decimal_places=2)