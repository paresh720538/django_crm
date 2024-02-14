from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import CreateUserForm,LoginForm,CreateRecordForm,UpdateRecordForm

# for logout and login
from django.contrib.auth.models import auth
from django.contrib.auth import authenticate

#this is required for sohw the dash board pageh without register or login a account
from django.contrib.auth.decorators import login_required

#add database record model in dashboard page
from .models import Record

#send success message to the user for register and login

from django.contrib import messages

# Create your views here.

# home page
def home(request):
    # return HttpResponse(" hello world !")
    return render(request,'webApp/home.html')

#Register 
def register(request):
    
    form = CreateUserForm()
    
    if request.method == "POST":
        
        form = CreateUserForm(request.POST)
        
        if form.is_valid():
            
            form.save()
            
            messages.success(request,"Account Created Successfully!")
            
            return redirect('login')

    context = {'form':form}
    return render(request, 'webApp/register.html',context=context)


#login  function
def login(request):
    form = LoginForm()
    
    if request.method == "POST":
        
        form = LoginForm(request, data=request.POST)
        
        if form.is_valid():
            username = request.POST.get('username')
            password = request.POST.get('password')
            
            user = authenticate(request, username = username , password = password)
            
            if user is not None:
                auth.login(request,user)
                
                messages.success(request," LoggedIn Successfully!")
                
                return redirect('dashboard')
          
    context = {'form':form}
    return render (request, 'webApp/login.html',context=context)
        
    
#logout function

def logout(request):
    
    auth.logout(request)
    
    messages.success(request,"Logout Successfully!")
    
    return redirect("login")


# DashBoard function

@login_required(login_url="login")
def dashboard(request):
    
    my_records = Record.objects.all()
    context = {'records': my_records}
    
    return render(request,"webApp/dashboard.html",context=context)

#CREATE A RECORD
@login_required(login_url='login')
def create_record(request):

    form = CreateRecordForm()

    if request.method == "POST":

        form = CreateRecordForm(request.POST)

        if form.is_valid():

            form.save()

            messages.success(request,"Record Created Successfully!")

            return redirect("dashboard")

    context = {'form': form}

    return render(request, 'webApp/create-record.html', context=context)

#Update record

@login_required(login_url='login')
def update_record(request, pk):
    record = Record.objects.get(id=pk)
    
    form = UpdateRecordForm(instance=record)
    
    if request.method == "POST":
        
        form = UpdateRecordForm(request.POST,instance=record)
        
        if form.is_valid():
            
            form.save()
            
            messages.success(request,"Record Updated Successfully!")
            
            return redirect('dashboard')
    context = {'form':form}
    
    return render(request,'webApp/update-record.html',context=context)


#Read/view a singile record
@login_required(login_url='login')
def view_record(request, pk):
    
    all_records = Record.objects.get(id=pk)
    
    context = {'record':all_records}
    
    return render(request,'webApp/view-record.html',context=context)


#Delete the record

@login_required(login_url='login')
def delete_record(request, pk):
    
    record = Record.objects.get(id=pk)
    
    record.delete()
    
    messages.success(request,"Record Deleted Successfully!")
    
    return redirect('dashboard')