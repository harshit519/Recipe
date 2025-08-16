from django.shortcuts import render, redirect, get_object_or_404
from .models import rcp
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required 

# Create your views here.

@login_required(login_url='/login/')
def receipes(request):
    if request.method == 'POST':
        data = request.POST

        img = request.FILES.get('rcp_image')
        a = data.get("rcp_name")
        c = data.get('rcp_description')
        

        rcp.objects.create(
            user=request.user,
            rcp_name=a,
            rcp_description=c,
            rcp_image=img,
        )
        
        return redirect('/receipes/')
    queryset = rcp.objects.select_related('user').all()
    context = {"rcp": queryset}
    return render(request, 'receipes.html', context)




@login_required(login_url='/login/')
def submit(request):
    queryset = rcp.objects.select_related('user').all()
    search_term = request.GET.get('search')
    if search_term:
        queryset = queryset.filter(rcp_name__icontains=search_term)
    return render(request, 'submit.html', context={"page": 'submit', 'rcp': queryset})



@login_required(login_url='/login/')
def delete(request, id):
    queryset = get_object_or_404(rcp, id=id)
    queryset.delete()
        
    return redirect('/submit/')



@login_required(login_url='/login/')
def update(request,id):
    queryset = get_object_or_404(rcp, id=id)
    if request.method == 'POST':
        data = request.POST

        img = request.FILES.get('rcp_image')
        a = data.get("rcp_name")
        c = data.get('rcp_description')

        if a:
            queryset.rcp_name=a
        if c:
            queryset.rcp_description=c
         

        if img:
            queryset.rcp_image=img
        queryset.save()

        return redirect('/submit/')
    
    context={'receipe':queryset}

    return render(request,'update_receipes.html',context)


def login_page(request):
    if request.method == 'POST':
        data = request.POST
        username=data.get('username')
        password=data.get('password')

        if not User.objects.filter(username=username).exists():
            messages.error(request,'invalid username')
            return redirect('/login/')
        
        user=authenticate(username=username,password=password)
        if user is None:
            messages.error(request,'invalid username or password')
            return redirect('/login/')

        else:
            login(request,user)
            return redirect('/receipes/')





    return render(request,'login.html')
    
def logout_page(request):
    logout(request)
    return redirect('/login/')





def register(request):
    if request.method == 'POST':
        data = request.POST


        
        first=data.get('first_name')
        last=data.get('last_name')
        username=data.get('Username')
        password=data.get('password')

        user=User.objects.filter(username=username)
        if user.exists():
            messages.error(request,'username is already taken')
            return redirect('/register/')

        user=User.objects.create(
           first_name =first,
           last_name=last,
           username=username,
                            )
        user.set_password(password)
        user.save()


        messages.info(request,'Account created successfully')

        return redirect('/register/')
    
    return render(request,'register.html')