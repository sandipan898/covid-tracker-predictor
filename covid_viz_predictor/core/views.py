from django.shortcuts import render, HttpResponse, render
import requests
import json
import datetime
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
        historical_worldwide_cases = historical_worldwide['cases']
        historical_worldwide_dates = list(historical_worldwide_cases.keys())
        historical_worldwide_cases = list(historical_worldwide_cases.values())
        historical_worldwide_recovered = list(historical_worldwide['recovered'].values())
        historical_worldwide_deaths = list(historical_worldwide['deaths'].values())
        # print(historical_worldwide_dates.count(), historical_worldwide_cases.count())
    except Exception as e:
        print(e)
        historical_worldwide = {}
    
    try:
        countries= requests.get("https://disease.sh/v3/covid-19/countries").json()
        print(countries[0])
    except Exception as e:
        print(e)
        countries = {}
    
    context = {
        'countries_data': countries,
        'all_data_worldwide': all_data_worldwide,
        'historical_worldwide_dates': historical_worldwide_dates,
        'historical_worldwide_cases': historical_worldwide_cases,
        'historical_worldwide_recovered': historical_worldwide_recovered,
        'historical_worldwide_deaths': historical_worldwide_deaths,
    }
    return render(request, template_name='dashboard.html', context=context)
