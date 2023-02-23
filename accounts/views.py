from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.contrib.auth.models import User
from contacts.models import Contact
from mainapp.models import *


def register(request):
    if request.method == 'POST':
        #Get form values
        comp_name = request.POST['comp_name']
        comp_email = request.POST['comp_email']
        comp_number = request.POST['comp_number']
        comp_logo = request.FILES.get('comp_logo')
        comp_domain = request.POST['comp_domain']
        comp_adress = request.POST['comp_adress']
        comp_city = request.POST['comp_city']
        description = request.POST['description']
        password = request.POST['password1']
        password2 = request.POST['password2']

        # Check if passwords match
        if password == password2:
            #  Check username
            if User.objects.filter(username=comp_name).exists():
                messages.error(request, 'The username already exists')
                return redirect('register')
            else:
                # if User.objects.filter(email=email).exists():
                #     messages.error(request, 'The email already exists')
                #     return redirect('register')
                # pass
                # else:
                    # Everything passed
                user = User.objects.create_user(username=comp_name, password=password, email=comp_email)
                # Login after register
                user.save()
                company = Company(comp_Name=comp_name,comp_mail=comp_email,comp_Number = comp_number, comp_Logo = comp_logo,comp_domain=comp_domain,comp_adress=comp_adress,comp_city=comp_city,description=description,active=True)
                company.save()
                
                messages.success(request, 'You are Company Succesfully registered and can Log In')
                return redirect('login')
        else:
            messages.error(request, 'Passwords do not match')
            return redirect('register')
    else:
        return render(request, 'accounts/register.html')


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            messages.success(request, 'You are now logged in')
            
            return redirect('dashboard')
        else:
            messages.error(request, 'Invalid credentials')
            return redirect('login')
    else:
        return render(request, 'accounts/login.html')


def logout(request):
    if request.method == "POST":
        auth.logout(request)
        messages.success(request, 'You are now logged out')
        return redirect('login')


def dashboard(request):
    user_contacts = Contact.objects.order_by('-contact_date').filter(user_id=request.user.id)
    company = Company.objects.get(comp_Name=request.user.username)
    context = {
        'contacts': user_contacts,
        'comp' : company
    }
    return render(request, 'accounts/dashboard.html', context)
