from django.db import models

# Create your models here.

class Booksbase(models.Model):
    BookId=models.AutoField(primary_key=True)
    BookName=models.CharField(max_length=500)
    BookPrice=models.CharField(max_length=500)
    BookpicName=models.CharField(max_length=500)