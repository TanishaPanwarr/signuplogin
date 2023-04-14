from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib import auth
def index(request):
    return render(request,"index.html")
def signup(request):
    #return render(request,"signup.html")
    if request.method=='POST':
        username=request.POST['username']
        firstname=request.POST['firstname']
        lastname=request.POST['lastname']
        email=request.POST['email']
        password=request.POST['password']
        address=request.POST['address']
        mobile=request.POST['mobile']
        if User.objects.filter(username=username).exists():
            messages.warning(request,"user name already exixt")
            return redirect("login")
        elif User.objects.filter(email=email).exists():
            messages.warning(request,"email aleady eist")
            return redirect("signup")
        else:
            user=User.objects.create_user(username=username,first_name=firstname,last_name=lastname,email=email,password=password)
            user.address=address
            user.mobile=mobile
            user.save()
            data=User.objects.all()
            #print(data)
            return render(request,'login.html',{'da':data})
    else:
        return render(request,'signup.html')
        
def login(request):
    if request.method=="POST":
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
              auth.login(request,user)
              return render (request,'home.html')
        else:
            messages.info(request,"successfully")
            #data=user.objects.all()
            #return render(request,'home.html',{'da':data})
            return render(request,'login.html')
    else:    
        return render(request,"login.html")
def logout(request):
    auth.logout(request)
    messages.success(request,"logout succesfully")
    return render(request,"index.html")
        