from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models
from django.utils import timezone
import uuid
from django.conf import settings
from django.core.mail import send_mail


class CustomUserManager(BaseUserManager):
    def create_user(self, fullName, doctorOrNurseID, role, department, email, contact, address, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(fullName=fullName, doctorOrNurseID=doctorOrNurseID, role=role, department=department,
                          email=email, contact=contact, address=address, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, fullName, doctorOrNurseID, role, department, email, contact, address, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self.create_user(fullName, doctorOrNurseID, role, department, email, contact, address, password, **extra_fields)

class CustomUser(AbstractBaseUser, PermissionsMixin):
    fullName = models.CharField(max_length=100)
    doctorOrNurseID = models.CharField(max_length=100, unique=True)
    role= models.CharField(max_length=100)
    department = models.CharField(max_length=100, blank=True)
    email = models.EmailField(unique=True)
    contact = models.CharField(max_length=100, blank=True, unique=True)
    address = models.CharField(max_length=100, blank=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    date_joined = models.DateTimeField(default=timezone.now)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['fullName', 'doctorOrNurseID', 'role', 'department', 'contact', 'address']

    def __str__(self):
        return self.email




class Patient(models.Model):
    patientName = models.CharField(max_length=255)
    ghCardNumber = models.CharField(max_length=255)
    patientID = models.CharField(max_length=8, unique=True, editable=False)
    email = models.EmailField(blank=True)
    address = models.TextField()
    contact = models.CharField(max_length=15)
    guardianContact = models.CharField(max_length=15)
    patientImg = models.ImageField(upload_to='patient_images/', null=True, blank=True)
    created_at = models.DateTimeField(default=timezone.now)

    def save(self, *args, **kwargs):
        if not self.patientID:
            self.patientID = str(uuid.uuid4())[:8]
        super(Patient, self).save(*args, **kwargs)
        
    def send_account_created_email(self):
        subject = 'Account Created Successfully'
        message = f'Hello {self.patientName},\n\nYour account with Patient ID {self.patientID} has been created successfully. Welcome to our Hospital!'
        from_email = settings.EMAIL_HOST_USER
        recipient_list = [self.email]

        send_mail(subject, message, from_email, recipient_list, fail_silently=False)


    def __str__(self):
        return self.patientName