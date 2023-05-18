from django.urls import path

from .views import view_closest_pair


urlpatterns = [
    path('', view_closest_pair, name="closest_point" )
]
