from django.shortcuts import render
import folium
from folium.plugins import FastMarkerCluster
from core.models import EVChargingLocation
from django.db.models import Avg


# Create your views here.
def index(request):
    avg_lat = EVChargingLocation.objects.aggregate(avg=Avg('latitude'))['avg']
    print(avg_lat)
    stations = EVChargingLocation.objects.all()
    # stations = EVChargingLocation.objects.exclude(latitude__gt=avg_lat)
    m = folium.Map(location=[41.5825, -72.699997], zoom_start=9)
        # for station in stations:
        #     coordinates = (station.latitude, station.longitude)
        #     folium.Marker(coordinates, popup=station.station_name).add_to(m)

    latitueds = [station.latitude for station in stations]
    longituedes = [station.longitude for station in stations]

    FastMarkerCluster(data=list(zip(latitueds, longituedes))).add_to(m)
    context = {'map': m._repr_html_()}
    return render(request, 'index.html', context)
