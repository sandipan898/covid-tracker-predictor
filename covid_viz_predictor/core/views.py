from django.shortcuts import render, HttpResponse, render
# Create your views here.

def dashboard_view(request):
    return render(request, template_name='dashboard.html')