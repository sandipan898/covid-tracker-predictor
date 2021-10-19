from django.shortcuts import render, HttpResponse, render
import requests
import json
# Create your views here.

def dashboard_view(request):
    # data = requests.get('https://corona.lmao.ninja/v2/all?yesterday')
    data = requests.get("https://disease.sh/v3/covid-19/all")
    # historical_worldwide = requests.get("https://corona.lmao.ninja/v2/historical/all")
    historical_worldwide = requests.get("https://disease.sh/v3/covid-19/historical/all?lastdays=all")
    # print(historical_worldwide.json())
    print(data.json())
    try:
        world_wide = data.json()
    except Exception as e:
        print(e)
        world_wide = {
            'cases': 0, 
            'recovered': 0,
            'deaths': 0
        }
    # print(json.loads(world_wide))
    return render(request, template_name='dashboard.html', context=world_wide)
