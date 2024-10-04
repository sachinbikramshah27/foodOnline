from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager


# Create your models here.
class UserManager(BaseUserManager):
    def create_user(self,first_name, last_name,username, email, password= None):
        if not email:
            raise ValueError('User must have an email address')
        if not username:
            raise ValueError("User must have a valid username")

        user = self.model(
                email= self.normalize_email(email),
                username = username,
                first_name= first_name,
                last_name=last_name
            )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, first_name, last_name, username, email, password=None):
        user = self.create_user(
            email=self.normalize_email(email),
            username=username,
            password=password,
            first_name=first_name,
            last_name=last_name
        )

        user.is_admin = True
        user.is_staff = True
        user.is_active = True
        user.is_superadmin = True

        user.save(using=self._db)
        return user
    

  
class User(AbstractBaseUser):
    VENDOR = 1
    CUSTOMER = 2

    ROLE_CHOICES =[
        (VENDOR,'Vendor'),
        (CUSTOMER,'Customer'),
    ]

    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    username = models.CharField(max_length=50,unique=True)
    email = models.EmailField(max_length=100,unique=True)
    phone_number = models.CharField(max_length=12,blank=True)
    role = models.PositiveSmallIntegerField(choices=ROLE_CHOICES,blank=True,null=True)

    #required fields
    created_date = models.DateTimeField(auto_now_add=True)
    joined_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)
    last_login = models.DateTimeField(auto_now=True)

    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    is_superadmin = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS =['username','first_name','last_name']

    objects = UserManager()

    def __str__(self):
        return self.email

    def has_perm(self, perm , object=None):
        return self.is_admin

    def has_module_perms(self,app_label):
        return True


class UserProfile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,null=True,blank=True)
    profile_picture = models.ImageField(upload_to='users/profile_pictures/',null=True,blank=True)
    cover_photo = models.ImageField(upload_to='users/cover_photos/',null=True,blank=True)
    address_line_1 = models.CharField(max_length=100,null=True,blank=True)
    address_line_2 = models.CharField(max_length=100,null=True,blank=True)
    country = models.CharField(max_length=100,null=True,blank=True)
    state = models.CharField(max_length=100,null=True,blank=True)
    city = models.CharField(max_length=100,null=True,blank=True)
    pin_code = models.CharField(max_length=8,null=True,blank=True)
    latitude = models.CharField(max_length=100,null=True,blank=True)
    longitude = models.CharField(max_length=100,null=True,blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.username




