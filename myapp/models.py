from django.db import models

# Create your models here.
class person(models.Model):
    user=models.CharField(max_length=20)
    email=models.EmailField()
    mobile=models.PositiveBigIntegerField()

class Automobile(models.Model):
    type=models.CharField(max_length=30)
    vname=models.CharField(max_length=40)
    cname=models.CharField(max_length=40)
    year=models.PositiveIntegerField()
    price=models.PositiveIntegerField()

    def __str__(self):
        return self.vname + '  ' +self.cname



