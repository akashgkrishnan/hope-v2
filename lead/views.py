from django.shortcuts import render

# Create your views here.
def lead_index(request):
    return render(request,'lead/lead-index.html')