from django.db import models

# Create your models here.


class Points(models.Model):
    points_data = models.CharField(max_length=255)
    closest_pair = models.CharField(max_length=255)

    class Meta:
        db_table = "points_table"

    def __str__(self) -> str:
        return f"{self.points_data} + {self.closest_pair}"


# {
#    "points":"1,2; 3,4;5,6"
# }