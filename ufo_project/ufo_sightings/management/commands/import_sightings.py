import os
import csv
from django.core.management.base import BaseCommand
from django.contrib.gis.geos import Point
from ufo_sightings.models import Sighting
from datetime import datetime

class Command(BaseCommand):
    help = 'Import UFO sightings from CSV'

    def handle(self, *args, **kwargs):
        csv_file_path = os.path.join('data', 'ufo_sightings.csv')

        # Check if the CSV file exists
        if not os.path.exists(csv_file_path):
            self.stdout.write(self.style.ERROR(f"File {csv_file_path} does not exist"))
            return

        with open(csv_file_path, 'r', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile, delimiter='\t')  # Assuming tab-delimited
            sightings_created = 0
            for row in reader:
                try:
                    datetime_str = row['Date_time']
                    dt = datetime.strptime(datetime_str, '%m/%d/%Y %H:%M')

                    date_documented_str = row['date_documented']
                    date_doc = datetime.strptime(date_documented_str, '%m/%d/%Y').date()

                    latitude = float(row['latitude'])
                    longitude = float(row['longitude'])
                    location = Point(longitude, latitude)

                    sighting = Sighting(
                        datetime=dt,
                        city=row['city'],
                        state_province=row.get('state/province') or None,
                        country=row['country'].lower(),
                        ufo_shape=row.get('UFO_shape') or None,
                        duration_seconds=float(row['length_of_encounter_seconds']),
                        duration_reported=row.get('described_duration_of_encounter') or None,
                        description=row['description'],
                        date_documented=date_doc,
                        location=location,
                    )
                    sighting.save()
                    sightings_created += 1
                except Exception as e:
                    self.stdout.write(self.style.ERROR(f"Error processing row: {e}"))
                    self.stdout.write(self.style.ERROR(f"Row data: {row}"))
            self.stdout.write(self.style.SUCCESS(f"Imported {sightings_created} sightings."))
