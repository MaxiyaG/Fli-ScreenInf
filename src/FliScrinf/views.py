from django.shortcuts import render
from datetime import datetime

def index(request):
    flight_type = request.POST.get('flightType', 'departure')
    airport = request.POST.get('airport', 'CDG')
    date = datetime.today()

    if flight_type == 'departure':
        flights = [
            {"flight_number": "AF123", "destination": "Paris", "status": "On time"},
            {"flight_number": "BA456", "destination": "London", "status": "Delayed"},
            # Ajoutez d'autres vols de départ ici
        ]
    else:
        flights = [
            {"flight_number": "AF789", "origin": "Paris", "status": "On time"},
            {"flight_number": "BA654", "origin": "London", "status": "Delayed"},
            # Ajoutez d'autres vols d'arrivée ici
        ]

    return render(request, 'index.html', context={"date": date, "airport": airport, "flights": flights})