from django.shortcuts import render

# Create your views here.
def forcondition(request):
    d={'name':'sunanda'}
    return render(request,'forcondition.html',d)
