from django.db import models
from django.core.exceptions import ValidationError
from django.core.validators import MinValueValidator, MaxValueValidator
from django.contrib.auth.models import User

def alphanumeric(value):
    if not str(value).isalnum():
        raise ValidationError('This field must contain only letters and numbers')
    return value

class Showroomlist(models.Model):
    name = models.CharField(max_length=30)
    location = models.CharField(max_length=100)
    website = models.URLField(max_length=100)

    def __str__(self):
        return self.name

# Create your models here.
class Carlist(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    activate = models.BooleanField(default=False)
    chassis_number = models.CharField(max_length=100, blank=True, null=True, validators=[alphanumeric])
    price = models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True)
    showroom = models.ForeignKey(Showroomlist, on_delete=models.CASCADE, related_name='showrooms',null=True)

    def __str__(self):
        return self.name
    
class Review(models.Model):
    apiuser = models.ForeignKey(User, on_delete=models.CASCADE,null=True)
    rating = models.IntegerField(validators=[MinValueValidator, MaxValueValidator])
    comments = models.CharField(max_length=200,null=True)
    car = models.ForeignKey(Carlist, on_delete=models.CASCADE, related_name='Reviews',null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "the rating of " + self.car.name + ": ---> " + str(self.rating)
