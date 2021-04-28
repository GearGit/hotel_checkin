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

# class UpdateView(View):
#     def get(self, request):
#         obj = CheckInModel.objects.all()  
#         return render(request,"update.html",{'dataObjects':obj})  

# class Delete(View):
#     def get(self,request,id):
#         obj = CheckInModel.objects.get(id=id)  
#         obj.delete()  
#         return redirect("/home")      

