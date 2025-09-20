from django.db import models
from django.contrib import admin
class Car(models.Model):
    car_id=models.IntegerField()
    car_name=models.CharField(max_length=100)
    company=models.CharField(max_length=50)
    year=models.IntegerField()
    price=models.FloatField()

class CarAdmin(admin.ModelAdmin):
    list_display=('car_id','car_name','company','year','price')


