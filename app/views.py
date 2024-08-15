from django.shortcuts import render

# Create your views here.
import datetime
def filters(request):
    dt=datetime.datetime.now()
    d={'data':'this IS BUIlt iN FIlters','dt':dt,'c':1}
    return render(request,'filters.html',d)

def user(request):
    d={'data':'TOday We ARE dealing with Userdefined FilTERs'}
    return render(request,'user.html',d)