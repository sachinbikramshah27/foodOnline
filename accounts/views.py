from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib import messages
from . forms import UserForm
from . models import User,UserProfile
from vendor.forms import VendorForm

# Create your views here.

def registerUser(request):
    if request.method == 'POST':
        # form = UserForm()
        print(request.POST)
        form = UserForm(request.POST)
        if form.is_valid():
            #Create User using the Form

            #commit- false --> ready to be saved not but commited
            # password = form.cleaned_data['password']
            # user =  form.save(commit=False)
            # user.set_password(password)
            # user.role = User.CUSTOMER
            # user.save()

            #Create User using the create_user
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = User.objects.create_user(
                first_name=first_name,
                last_name= last_name,
                username=username,
                email=email,
                password=password
            )
            user.role = User.CUSTOMER
            user.save()
            messages.success(request,"Your account has been registered")


            return redirect('registerUser')
        else:
            print("Invalid form")
            print(form.errors)

    else:
        form = UserForm()

    context = {
        'form': form
    }
    return render(request,'accounts/register_user.html',context)




def registerVendor(request):
    
    # form = UserForm()
    # vendor_form = VendorForm()
    if request.method == 'POST':
        
        form = UserForm(request.POST)
        vendor_form = VendorForm(request.POST,request.FILES)
        if form.is_valid() and vendor_form.is_valid():
            
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = User.objects.create_user(
                first_name=first_name,
                last_name= last_name,
                username=username,
                email=email,
                password=password
            )
            user.role = User.VENDOR
            user.save() 
            #vendor  
            vendor = vendor_form.save(commit=False)
            vendor.user = user
            user_profile= UserProfile.objects.get(user=user)
            vendor.user_profile = user_profile
            vendor.save()
            messages.success(request,"You have successfully registered your vendor account")
            return redirect('registerVendor')
        else:
            print("Invalid Forms") 
    else:
        form = UserForm()
        vendor_form = VendorForm()   
            



    context ={
        'form': form,
        'vendor_form': vendor_form
    }


    return render(request,'accounts/register_vendor.html',context)