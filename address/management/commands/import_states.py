import json
from django.core.management.base import BaseCommand
from address.models import State  # Import your model


class Command(BaseCommand):
    help = 'Populates the State table with data from a JSON file'

    def handle(self, *args, **kwargs):
        # Define the path to your JSON file
        json_file_path = 'data/state.json'

        # Open and read the JSON file
        with open(json_file_path, 'r', encoding='utf-8') as file:
            data = json.load(file)

        # Iterate over the data and create State objects
        for item in data:
            state_name = item['name']
            state_id = item['id']

            # Create or update the State entry
            state, created = State.objects.update_or_create(
                id=state_id,
                defaults={'name': state_name}
            )

            if created:
                self.stdout.write(self.style.SUCCESS(f"Added state: {state_name}"))
            else:
                self.stdout.write(self.style.SUCCESS(f"Updated state: {state_name}"))

        self.stdout.write(self.style.SUCCESS("Database population complete."))
