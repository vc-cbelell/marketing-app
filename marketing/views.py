from django.shortcuts import render

# Create your views here.
def Index(request):
    return render(request, 'index.html')

def Page1(request):
    return render(request, 'page1.html')