from django.shortcuts import render
from .models import Student
from django.http import HttpResponse

# Create your views here.
def Students(request):
    if request.method=='POST':
        data=request.POST
        name1=data['name']
        age=data['age']
        email=data['email']
        phone=data['phone']
        reg=Student(name=name1,age=age,email=email,phone=phone)
        reg.save()
        return HttpResponse("successfully register") 
    return render(request,'index.html')
