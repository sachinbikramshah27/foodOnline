from django.db import models
from django.conf import settings

# Create your models here.

class Vendor(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL,related_name='user',on_delete=models.CASCADE)
    #here i used string reference of accounts.UserProfile, instead of import 
    #from another app
    user_profile = models.OneToOneField('accounts.UserProfile',related_name='userprofile',on_delete=models.CASCADE)
    vendor_name = models.CharField(max_length=100)
    vendor_license = models.ImageField(upload_to='vendor/license')
    is_approved = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.vendor_name