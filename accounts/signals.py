from django.db.models.signals import post_save,pre_save
from django.dispatch import receiver
from .models import User,UserProfile

@receiver(post_save,sender=User)
def post_save_create_profile_receiver(sender,instance,created,**kwargs):
    print("This is django signals ---> post_save function")
    print("<--------***************---------->")

    #this will create the userprofile as soon as user is created
    if created:
            UserProfile.objects.create(user=instance)
    else:
             #update case  
        try:
                profile = UserProfile.objects.get(user=instance)
                profile.save()
        except:
                #user was already created but userprofile didnt exist,so need to create one case
                UserProfile.objects.create(user=instance)

    

    
@receiver(pre_save,sender=User)
def pre_save_user__profile(sender,instance,**kwargs):
    print("This is django signals ---> pre_save function")
    print("<--------***************---------->")
    print(instance.username , 'is being created')