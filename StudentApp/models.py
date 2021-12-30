from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField(max_length=30)
    phone = models.CharField(max_length=30)
    gender = models.CharField(max_length=10)
    d_o_b = models.DateField(max_length=30)
    address = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class GetImage(models.Model):
    img_title = models.CharField(max_length=20)
    img = models.ImageField(upload_to="media")
    class Meta:
        db_table = "gallery"
