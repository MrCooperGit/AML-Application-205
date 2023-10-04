from django.db import models

# Create your models here.


class Customer(models.Model):
    id = models.AutoField(primary_key=True)
    full_name = models.CharField(max_length=100)
    date_of_birth = models.DateField()
    address = models.CharField(max_length=200)
    phone = models.IntegerField()
    email = models.EmailField(max_length=50)
    identity_verified = models.BooleanField(default=False, null=True)
    address_verified = models.BooleanField(default=False, null=True)
    additional_info = models.CharField(max_length=500, null=True)

    class Meta:
        ordering = ('full_name',)

    def __str__(self):
        return self.full_name


class Company(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    company_registration_num = models.IntegerField(unique=True)
    address = models.CharField(max_length=200)

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name


class Director(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)

    def __str__(self):
        return self.customer


class Shareholder(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)

    def __str__(self):
        return self.customer


class Active_Sessions(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20)
    url = models.URLField(null=False, max_length=200)

    def __str__(self):
        return self.id
