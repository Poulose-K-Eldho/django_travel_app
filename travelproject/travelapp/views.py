from django.shortcuts import render
from .models import foods
# Create your views here.
def fun(request):
    obj=foods.objects.all()

    return render(request,'index.html',{'results':obj})
def detail(request,foods_id):
    product1=foods.objects.get(id=foods_id)
    return render(request,'detail.html',{'obj':product1})