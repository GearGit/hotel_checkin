from django.shortcuts import render
from django.template import RequestContext
# Create your views here.

from .forms import CheckInModel

def homePage(request):
    return render(request,'home.html')

def setCheckInView(request):
    # form = CheckInModel(request.POST)
    # if request.method == "POST":
    #     form = CheckInModel(request.POST)
    #     if form.is_valid():
    #         form.save()

    # context = {'form':form}
    
    # return render(request,'checkin_form.html'.context)

    if request.method == 'POST':
        form = CheckInModel(request.POST)
        if form.is_valid():
            new_hardware = form.save()
            return render('checkin_form.html')
    else:
        form = CheckInModel()

        return render(None,'checkin_form.html', {'form': form})