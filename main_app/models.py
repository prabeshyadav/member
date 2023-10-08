from django.db import models
from .manager import CustomUserManager
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin

# Create your models here.



class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    is_verified=models.BooleanField(default=True)
    otp=models.CharField(max_length=200,null=True,blank=True)
    organization_name = models.CharField(max_length=255)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    phone_number = models.CharField(max_length=15)
    subdomain = models.CharField(max_length=50, unique=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    date_joined = models.DateTimeField(auto_now_add=True)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['organization_name', 'first_name', 'last_name', 'phone_number', 'subdomain']

    def __str__(self):
        return self.email


# class OrganizationSetup(models.Model):
#     org_name=models.CharField(max_length=225)
#     org_description=models.CharField(max_length=225)
#     address=models.CharField(max_length=225)
#     website=models.CharField(max_length=225)
#     phone=models.CharField(max_length=225)
#     email=models.CharField(max_length=225)
#     establish_date=models.DateTimeField()
#     founder=models.CharField(max_length=225)
#     logo=models.ImageField()
#     banner_image=models.ImageField()
#     payment_mode=models.BooleanField()
    

# class MemberSetup(models.Model):
#     membershipIdpPrefix=models.CharField(max_length=225)
#     root_word=models.CharField(max_length=225)
#     membershipIdSufix=models.CharField(max_length=225)
    
# class UsersSetup(models.Model):
#     superAdmin=models.CharField(max_length=225)
#     admin=models.CharField(max_length=225)
#     manager=models.CharField(max_length=225)
#     users=models.CharField(max_length=225)
    
# class PaymentSetup(models.Model):
#     esewa=models.BooleanField()
#     khalti=models.BooleanField()
#     imepay=models.BooleanField()
#     bank_deposit=models.BooleanField()


# class CommunicationSetup(models.Model):
#     to_admin=models.CharField(max_length=225)
#     to_org=models.CharField(max_length=225)
#     to_users=models.CharField(max_length=225)