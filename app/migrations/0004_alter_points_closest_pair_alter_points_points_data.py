# Generated by Django 4.2.1 on 2023-05-17 15:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_rename_points_points_points_data'),
    ]

    operations = [
        migrations.AlterField(
            model_name='points',
            name='closest_pair',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='points',
            name='points_data',
            field=models.CharField(max_length=255),
        ),
    ]
