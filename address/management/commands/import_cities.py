import json
from django.core.management.base import BaseCommand
from address.models import City, State

class Command(BaseCommand):
    help = 'Populates the City table with data from a JSON file'

    def handle(self, *args, **kwargs):
        json_file_path = 'data/cities.json'

        with open(json_file_path, 'r', encoding='utf-8-sig') as file:
            data = json.load(file)

        for i in range(len(data['state'])):
            city_name = data['name'][i]
            city_id = data['id'][i]
            state_pk = data['state_pk'][i]

            try:
                state = State.objects.get(id=state_pk)
            except State.DoesNotExist:
                self.stdout.write(self.style.ERROR(f"State with id {state_pk} does not exist. Skipping city: {city_name}"))
                continue

            city, created = City.objects.update_or_create(
                id=city_id,
                defaults={'name': city_name, 'state': state}
            )

            if created:
                self.stdout.write(self.style.SUCCESS(f"Added city: {city_name}"))
            else:
                self.stdout.write(self.style.SUCCESS(f"Updated city: {city_name}"))

        self.stdout.write(self.style.SUCCESS("City database population complete."))
