from django.db import models

# Create your models here.
class Person(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=15)
    date_of_birth = models.DateField()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Referral(models.Model):
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    referral_date = models.DateField()
    referrer_name = models.CharField(max_length=100)
    reason = models.CharField(max_length=100)
    note = models.TextField()
    document = models.FileField()

    def __str__(self):
        return f"Person's Full Name: {self.person.first_name} {self.person.last_name}, Referral Date: {self.referral_date}"
