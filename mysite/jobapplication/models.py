from django.db import models

# Create your models here.

#create your database models here.
class form(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    date = models.DateField()
    occupation = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

