from django.db import models


# Create your models here.


class Cohort(models.Model):
    numbers = models.IntegerField(default=0, unique=True)
    name = models.CharField(max_length=50, unique=True)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


3
GENDER = (
    ('M', 'Male'),
    ('F', 'Female'),
    ('O', 'Others')
)


class Natives(models.Model):
    e_mail = models.EmailField(unique=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    number = models.CharField(max_length=20, unique=True)
    gender = models.CharField(max_length=10, choices=GENDER, default='O')
    date_of_birth = models.DateField()
    date_created = models.DateTimeField(auto_now_add=True)
    cohort = models.ForeignKey(Cohort, on_delete=models.CASCADE)

    def __str__(self):
        return self.first_name + " " + self.last_name
