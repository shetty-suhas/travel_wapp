# Generated by Django 5.1.3 on 2024-11-07 10:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cab_booking', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='cabbooking',
            name='distance',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=6),
        ),
        migrations.AlterField(
            model_name='cab',
            name='base_fare',
            field=models.DecimalField(decimal_places=2, max_digits=5),
        ),
        migrations.AlterField(
            model_name='cab',
            name='per_km_rate',
            field=models.DecimalField(decimal_places=2, max_digits=5),
        ),
        migrations.AlterField(
            model_name='cabbooking',
            name='drop_location',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='cabbooking',
            name='pickup_location',
            field=models.CharField(max_length=100),
        ),
    ]
