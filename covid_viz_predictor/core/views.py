from django.shortcuts import render, HttpResponse, render
import requests
import json
# Create your views here.

def dashboard_view(request):
    data = requests.get('https://corona.lmao.ninja/v2/all?yesterday')
    world_wide = data.json()
    # print(json.loads(world_wide))
    return render(request, template_name='dashboard.html', context=world_wide)
