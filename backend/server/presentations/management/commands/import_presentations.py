import os

from django.core.management.base import BaseCommand
from django.utils.translation import gettext as _

from services.presentations_parser import PresentationsParser


class Command(BaseCommand):
    help = _("Import Presentations from JSON file")

    def add_arguments(self, parser):
        parser.add_argument("json_file", type=str, help=_("The path to the JSON file to be imported"))

    def handle(self, *args, **options):
        path = options["json_file"]
        if not os.path.isfile(path):
            self.stdout.write(self.style.ERROR("File '%s' does not exist" % path))
            return

        parser = PresentationsParser(path)
        parser.parse_and_save()
        self.stdout.write(self.style.SUCCESS(_("Successfully imported presentations data")))
