from django.shortcuts import render_to_response, get_list_or_404
from crimemap.mapper.models import Crime

def crime_by_type(request, crimeType):
    crime_list = get_list_or_404(Crime, type=crimeType)
    return render_to_response('crime_by_type.html', {'crime_list': crime_list})
