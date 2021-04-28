from django.shortcuts import render,redirect
from django.views import View
from .models import CheckInModel

# Create your views here.

from .forms import CheckInForm

class InitialView(View):
    def get(self, request):
        return redirect('/home')

class HomeView(View):
     def get(self, request):
        obj = CheckInModel.objects.all()  
        return render(request,"home.html",{'dataObjects':obj}) 

class CheckInView(View):
    def get(self,request):
        form = CheckInForm()
        return render(request,'checkin_form.html',{'form':form})
    
    def post(self,request):
        form = CheckInForm(request.POST,request.FILES)
        print(form.errors)
        if form.is_valid():
            form.save()
            return redirect('/home')

class UpdateView(View):
    def get(self, request,id):
        obj = CheckInModel.objects.get(id=id)  
        return render(request,"update.html",{'data':obj})  

    def post(self,request,id):
        obj = CheckInModel.objects.get(id=id)  
        for i in request.POST:
            if i == 'csrfmiddlewaretoken':
                continue
            if i == 'first_name':
                if obj.first_name != request.POST['first_name']:
                    obj.first_name = request.POST['first_name']
            if i == 'last_name':
                if obj.last_name != request.POST['last_name']:
                    obj.last_name = request.POST['last_name']
            if i == 'email':
                if obj.email != request.POST['email']:
                    obj.email = request.POST['email']
            if i == 'age':
                if obj.age != request.POST['age']:
                    obj.age = request.POST['age']
            if i == 'gender':
                if obj.gender != request.POST['gender']:
                    obj.gender = request.POST['gender']
            if i == 'address':
                if obj.address != request.POST['address']:
                    obj.address = request.POST['address']
            if i == 'checkin':
                if obj.checkin != request.POST['checkin'] and request.POST['checkin'] != '':
                    obj.checkin = request.POST['checkin']
            if i == 'checkout':
                if obj.checkout != request.POST['checkout'] and request.POST['checkout'] != '':
                    obj.checkout = request.POST['checkout']
            if i == 'payment_method':
                if obj.payment_method != request.POST['payment_method']:
                    obj.payment_method = request.POST['payment_method']
            if i == 'room_allocated':
                if obj.room_allocated != request.POST['room_allocated']:
                    obj.room_allocated = request.POST['room_allocated']
            if i == 'additional_choices':
                if obj.additional_choices != request.POST['additional_choices']:
                    obj.additional_choices = request.POST['additional_choices']
            if i == 'file_field':
                if request.POST['file_field'] != '':
                    obj.file_field = request.FILES['file_field']
        for i in request.FILES:
            if i == 'file_field':
                if request.FILES['file_field'] != '':
                    obj.file_field = request.FILES['file_field']
        obj.save()
        return redirect("/home")  

class DeleteView(View):
    def get(self,request,id):
        obj = CheckInModel.objects.get(id=id)  
        obj.delete()  
        return redirect("/home")      

