from django.shortcuts import render,redirect
from django.contrib.auth.models import User
import random
import string
# Create your views here.
from django.contrib import messages

from .models import *
def get_username():
  username = ''
  while True:
      username = ''.join(random.choice(string.ascii_letters + string.digits) for i in range(8))
      if User.objects.filter(username=username).count() == 0:
          break
  return username


def get_password():
  password = ''.join(random.choice(string.ascii_letters + string.digits) for i in range(8))
  return password
  
          
def generate_user():
  user = User()
  user.username = get_username()
  user.set_password(get_password())
  user.save()
  print(user)
  
  return user

def add_broker(request):
  if request.user.is_authenticated:
    if request.method == 'POST' and request.FILES['photo']:
      try:
        company = Company.objects.get(comp_Name=request.user.username)
        name = request.POST['name']
        lastname = request.POST['lastname']
        email = request.POST['email']    
        phone = request.POST['phone']
        description = request.POST['description']
        photo = request.FILES['photo']
        print(photo)
        model = Broker(user= generate_user(), name=name,lastname=lastname,email=email,phone=phone,description=description,photo=photo,active=True)
        model.save()
        company.brokers.add(model)
        company.save()

      
        return redirect('dashboard')
      except:
        pass
    
  return redirect('dashboard')


def add_properties(request):

    if request.method == 'POST' and request.FILES['properties'] :
      title = request.POST['title']
      types  =request.POST['types']
      city  = request.POST['city']
      adress = request.POST['adress']
      living_area = request.POST['living_area']
      land_size = request.POST['land_size']
      rooms = request.POST['rooms']
      price = request.POST['price']
      date_time1 = request.POST['date_time1']
      date_time2 = request.POST['date_time2']
      date_time3 = request.POST['date_time3']
      properties = request.FILES['properties']
      description = request.POST['description']
      date_time = date_helper(date_time=date_time1)
      date_time.save()
      date_time1 = date_helper(date_time=date_time2)
      date_time1.save()
      date_time2 = date_helper(date_time=date_time3)
      date_time2.save()
      model = Properties( title=title,types=types,city=city,
      adress=adress,living_area=living_area,land_size=land_size,rooms=rooms,price=price,properties=properties,description=description)
      model.save()

      model.date_time.add(date_time)
      model.save()
      model.date_time.add(date_time1)
      model.save()
      model.date_time.add(date_time2)
      model.save()

      return redirect('dashboard')
    else:
      return render(request,'mainapp/add_properties.html')
 
def view_properties(request):
  properties = Properties.objects.all()
  context = {
    'properties': properties
  }
  return render(request,'mainapp/view_properties.html',context)

def edit_properties(request,pk):
  properties = Properties.objects.filter(pk=pk)
  if properties.count() == 1:
      properties = properties[0]
      if request.method == "POST" and request.FILES['properties'] :
          title = request.POST['title']
          types  =request.POST['types']
          city  = request.POST['city']
          adress = request.POST['adress']
          living_area = request.POST['living_area']
          land_size = request.POST['land_size']
          rooms = request.POST['rooms']
          price = request.POST['price']
          date_time1 = request.POST['date_time1']
          date_time2 = request.POST['date_time2']
          date_time3 = request.POST['date_time3']
          properties = request.FILES['properties']
          description = request.POST['description']
          date_time = date_helper(date_time=date_time1)
          date_time.save()
          date_time1 = date_helper(date_time=date_time2)
          date_time1.save()
          date_time2 = date_helper(date_time=date_time3)
          date_time2.save()
          properties.title = title
          properties.types = types
          properties.adress = adress
          properties.city = city
          properties.living_area = living_area
          properties.land_size = land_size
          properties.rooms = rooms
          properties.price = price
          properties.description = description
          properties.save()
          return redirect(f'/inventory/view_properties')
       
  return render(request,'mainapp/view_properties.html',context)

def delete_properties(request,pk):
    try:
        record = Properties.objects.get(pk=pk)
        record.delete()
        messages.success(request, "Successfully Deleted category")
        return redirect(f'/inventory/view_properties')
    except:
        messages.error(request, "Record doesn't exists")
        return redirect(f'/inventory/view_properties')
