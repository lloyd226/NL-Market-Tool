# myapp/management/commands/remove_duplicates.py
from django.core.management.base import BaseCommand
from pub_priv_school_ls.models import School
from django.db.models import Count

class Command(BaseCommand):
    help = 'Remove duplicate items based on shchool name'

    def handle(self, *args, **kwargs):
        # Find duplicates
        duplicates = School.objects.values("school_name").annotate(school_name_count=Count("school_name")).filter(school_name_count__gt=1)

        for duplicate in duplicates:
            items = School.objects.filter(school_name=duplicate["school_name"])
            for item in items[1:]:  # Keep the first occurrence and delete the rest
                item.delete()

        self.stdout.write(self.style.SUCCESS('Successfully removed duplicates'))
