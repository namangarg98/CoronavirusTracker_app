from django.shortcuts import render
import requests
# Create your views here.


def home(request):
    url = "https://covid-193.p.rapidapi.com/statistics"
    q = request.GET.get('search')
    # err_msg = ''
    # name = "India"
    query = {"country": q}

    headers = {
        'x-rapidapi-host': "covid-193.p.rapidapi.com",
        'x-rapidapi-key': "82b8009890mshe2e74eb0e4fbe7cp18bfe5jsn03104478e2a4"
    }

    response = requests.request(
        "GET", url, headers=headers, params=query).json()
    # data = response.text
    # print(response)
    d = response['response']
    s = d[0]
    # print(s)
    if s['time'] is not None:
        context = {
            'name': q,
            'pop': s['population'],
            'all': s['cases']['total'],
            'recovered': s['cases']['recovered'],
            'deaths': s['deaths']['total'],
            'new': s['cases']['new'],
            'critical': s['cases']['critical'],
        }
        return render(request, 'index.html', context)
