# myapp/management/commands/delete_all_model_data.py
from django.core.management.base import BaseCommand
from pub_priv_school_ls.models import School  # Replace with your model

class Command(BaseCommand):
    help = 'Delete all instances of School'

    def handle(self, *args, **kwargs):
        School.objects.all().delete()
        self.stdout.write(self.style.SUCCESS('Successfully deleted all instances of School'))
