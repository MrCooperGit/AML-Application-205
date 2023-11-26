from django.db import models
from django.utils import timezone
from django.contrib.auth.models import Group, Permission
from django.contrib.auth.models import User, AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.conf import settings


# Create your models here.


class Entity(models.Model):
    name = models.CharField(max_length=100)
    users = models.ManyToManyField(User)

    class Meta:
        ordering = ('name',)
        verbose_name_plural = 'Registered Entities'

    def __str__(self):
        return self.name


class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        return self.create_user(email, password, **extra_fields)


class UserProfile(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='userprofile')
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


class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    entity = models.ForeignKey(Entity, on_delete=models.CASCADE)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    # Add other required fields

    # clash in the reverse accessor names for the groups and user_permissions fields between the auth.User model (Django's built-in User model) and your base_app.CustomUser model
    permissions = (
        ("view_customuser", "Can view custom users"),
    )
    groups = models.ManyToManyField(
        Group,
        verbose_name=('groups'),
        blank=True,
        help_text=('The groups this user belongs to.'),
        related_name='custom_users',  # Custom related_name
    )
    user_permissions = models.ManyToManyField(
        Permission,
        verbose_name=('user permissions'),
        blank=True,
        help_text=('Specific permissions for this user.'),
        related_name='custom_users_permissions',  # Custom related_name
    )

    class Meta:
        ordering = ('last_name',)

    def __str__(self):
        return self.email


class Customer(models.Model):
    id = models.AutoField(primary_key=True)
    entity = models.ForeignKey(Entity, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=100)
    date_of_birth = models.DateField()
    address = models.CharField(max_length=200)
    phone = models.IntegerField()
    email = models.EmailField(max_length=50)
    company = models.ForeignKey(
        'Company', on_delete=models.CASCADE, null=True, blank=True)
    customer_created_time = models.DateTimeField(auto_now_add=True)
    identity_verified = models.BooleanField(default=False, null=True)
    proof_of_identity = models.FileField(
        upload_to='customer_documents/identity/', null=True, blank=True)
    identity_verified_time = models.DateTimeField(auto_now_add=True)
    address_verified = models.BooleanField(default=False, null=True)
    proof_of_address = models.FileField(
        upload_to='customer_documents/address/', null=True, blank=True)
    address_verified_time = models.DateTimeField(auto_now_add=True)
    additional_info = models.CharField(max_length=500, blank=True)

    def save(self, *args, **kwargs):
        update_verification_times = kwargs.pop(
            'update_verification_times', True)

        if update_verification_times:
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
    company_registration_num = models.BigIntegerField(unique=True)
    address = models.CharField(max_length=200)

    class Meta:
        ordering = ('name',)
        verbose_name_plural = 'Companies'

    def __str__(self):
        return self.name


class Director(models.Model):
    entity = models.ForeignKey(Entity, on_delete=models.CASCADE)
    customer = models.OneToOneField(Customer, on_delete=models.CASCADE)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)

    def __str__(self):
        return self.customer.full_name


class Shareholder(models.Model):
    entity = models.ForeignKey(Entity, on_delete=models.CASCADE)
    customer = models.OneToOneField(Customer, on_delete=models.CASCADE)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)

    def __str__(self):
        return self.customer.full_name


class Active_Session(models.Model):
    # active session will be for storing forms on an entity level
    id = models.AutoField(primary_key=True)
    entity = models.ForeignKey(Entity, on_delete=models.CASCADE)

    def __str__(self):
        return self.id


class AvailableApps(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    display_name = models.CharField(max_length=100)

    class Meta:
        ordering = ('name',)
        verbose_name_plural = 'Available Apps'

    def __str__(self):
        return self.name
