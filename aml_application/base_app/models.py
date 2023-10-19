from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.


class Entity(models.Model):
    name = models.CharField(max_length=100)
    users = models.ManyToManyField(User)
    
    class Meta:
        ordering = ('name',)
        verbose_name_plural = 'Registered Entities'

    def __str__(self):
        return self.name


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    entity = models.ForeignKey(Entity, on_delete=models.CASCADE)
    USER_TYPE_CHOICES = [
        ('tAcsp', 'Trust or Company Service Provider'),
        ('fiAc', 'Financial Institutions or Casino'),
        ('lAc', 'Lawyer or Conveyancer'),
        ('accountants', 'Accountant'),
        ('rea', 'Real Estate Agent'),
        ('hvd', 'High Value Dealer'),
        ('tab', 'TAB New Zealand'),
        ('vasp', 'Virtual Asset Service Provider'),
    ]
    user_type = models.CharField(max_length=20, choices=USER_TYPE_CHOICES)

    def __str__(self):
        return self.user_type


class Customer(models.Model):
    id = models.AutoField(primary_key=True)
    entity = models.ForeignKey(Entity, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=100)
    date_of_birth = models.DateField()
    address = models.CharField(max_length=200)
    phone = models.IntegerField(default=123)
    email = models.EmailField(max_length=50)
    customer_created_time = models.DateTimeField(auto_now_add=True)
    identity_verified = models.BooleanField(default=False, null=True)
    proof_of_identity = models.FileField(
        upload_to='customer_documents/identity/', null=True, blank=True)
    identity_verified_time = models.DateTimeField(auto_now_add=True)
    address_verified = models.BooleanField(default=False, null=True)
    proof_of_address = models.FileField(
        upload_to='customer_documents/address/', null=True, blank=True)
    address_verified_time = models.DateTimeField(auto_now_add=True)
    additional_info = models.CharField(max_length=500, null=True)

    def save(self, *args, **kwargs):
        if self.identity_verified:
            self.identity_verified_time = timezone.now()
        else:
            self.identity_verified_time = None

        if self.address_verified:
            self.address_verified_time = timezone.now()
        else:
            self.address_verified_time = None

        super(Customer, self).save(*args, **kwargs)

    class Meta:
        ordering = ('full_name',)

    def __str__(self):
        return self.full_name


class Company(models.Model):
    id = models.AutoField(primary_key=True)
    entity = models.ForeignKey(Entity, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    company_registration_num = models.IntegerField(unique=True)
    address = models.CharField(max_length=200)

    class Meta:
        ordering = ('name',)
        verbose_name_plural = 'Companies'

    def __str__(self):
        return self.name


class Director(models.Model):
    entity = models.ForeignKey(Entity, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)

    def __str__(self):
        return self.customer


class Shareholder(models.Model):
    entity = models.ForeignKey(Entity, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)

    def __str__(self):
        return self.customer

class Active_Session(models.Model):
    # active session will be for storing forms on an entity level
    id = models.AutoField(primary_key=True)
    entity = models.ForeignKey(Entity, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.id
    
class AvailableApps(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)

    class Meta:
        ordering = ('name',)
        verbose_name_plural = 'Available Apps'
        
    def __str__(self):
        return self.name 