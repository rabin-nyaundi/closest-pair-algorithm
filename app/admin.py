from django.contrib import admin
from .models import Points

# Register your models here.
class PointsAdmin(admin.ModelAdmin):
    list_display = ("id","points_data", "closest_pair")


admin.site.register(Points, PointsAdmin)
