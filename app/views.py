from django.shortcuts import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
import json

from .utils import ClosestPair

from .utils import clean_data

from .models import Points

# Create your views here.

@api_view(['POST'])
def view_closest_pair(request):
    points_data = request.data.get('points')
    
    cleaned_data = clean_data(points_data)
    closest_pair = ClosestPair(cleaned_data)
    pair = closest_pair.divide_and_conquer(cleaned_data)
    
    points = Points()
    points.points_data = points_data
    points.closest_pair = pair
    points.save()

    return Response({"success": True})
