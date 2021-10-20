from django.shortcuts import render, HttpResponse, render
import requests
import json
# Create your views here.

def dashboard_view(request):
    try:
        # data = requests.get('https://corona.lmao.ninja/v2/all?yesterday')
        all_data_worldwide = requests.get("https://disease.sh/v3/covid-19/all").json()
    except Exception as e:
        print(e)
        world_wide = {
            'cases': 0, 
            'recovered': 0,
            'deaths': 0
        }

    try:
        # historical_worldwide = requests.get("https://corona.lmao.ninja/v2/historical/all")
        historical_worldwide = requests.get("https://disease.sh/v3/covid-19/historical/all?lastdays=all").json()
        historical_worldwide = json.dumps(historical_worldwide)
        print(historical_worldwide)
    except Exception as e:
        print(e)
        historical_worldwide = {}
    
    context = {
        'all_data_worldwide': all_data_worldwide,
        'historical_worldwide': historical_worldwide
    }
    return render(request, template_name='dashboard.html', context=context)
