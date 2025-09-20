# Ex02 Django ORM Web Application
## Date: 20.09.25

## AIM
To develop a Django application to store and retrieve data from a Movies Database using Object Relational Mapping(ORM).

## DESIGN STEPS

### STEP 1:
Clone the problem from GitHub

### STEP 2:
Create a new app in Django project

### STEP 3:
Enter the code for admin.py and models.py

### STEP 4:
Execute Django admin and create details for 10 books

## PROGRAM
~~~
admin.py

from django.contrib import admin
from .models import Car,CarAdmin
admin.site.register(Car,CarAdmin)

models.py

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

~~~

## OUTPUT
![alt text](<Screenshot 2025-09-20 111849.png>)



## RESULT
Thus the program for creating movies database using ORM hass been executed successfully
