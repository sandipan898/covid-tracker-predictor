from django.shortcuts import render, HttpResponse, render
import requests
import json
import datetime
# Create your views here.

def dashboard_view(request):
    try:
        # historical_worldwide = requests.get("https://corona.lmao.ninja/v2/historical/all")
        historical_worldwide = requests.get("https://disease.sh/v3/covid-19/historical/all?lastdays=all").json()
        historical_worldwide_cases = historical_worldwide['cases']
        historical_worldwide_dates = list(historical_worldwide_cases.keys())[::3]
        historical_worldwide_cases = list(historical_worldwide_cases.values())[::3]
        historical_worldwide_recovered = list(historical_worldwide['recovered'].values())[::3]
        historical_worldwide_deaths = list(historical_worldwide['deaths'].values())[::3]
        # print(historical_worldwide_dates[0])
    except Exception as e:
        print(e)
        historical_worldwide = {}
    
    try:
        countries= requests.get("https://disease.sh/v3/covid-19/countries").json()
        # flag_list = [country['countryInfo']['flag'] for country in countries]
    except Exception as e:
        print(e)
        countries = {}
        flag_list ={}

    context = {
        'countries_data': countries,
        # 'flag_list': flag_list,
        'historical_worldwide_dates': historical_worldwide_dates,
        'historical_worldwide_cases': historical_worldwide_cases,
        'historical_worldwide_recovered': historical_worldwide_recovered,
        'historical_worldwide_deaths': historical_worldwide_deaths,
    }
    return render(request, template_name='dashboard.html', context=context)
