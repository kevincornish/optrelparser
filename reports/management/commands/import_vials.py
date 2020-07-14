import os

from django.core.management.base import BaseCommand

from reports.models import Vial
from reports.importers.report import VialImporter


class Command(BaseCommand):
    def handle(self, *args, **options):
        if options['truncate']:
            Vial.objects.all().delete()
        processor = VialImporter()
        processor.import_directory(options['directory'])

    def add_arguments(self, parser):
        parser.add_argument("-d", "--dir", action="store", dest="directory", type=str, default='files/vials')
        parser.add_argument("--truncate", action="store_true", dest="truncate", default=False)
        return parser

    def get_pdfs(self, directory):
        return [f'{directory}/{_file}' for _file in os.listdir(directory) if
                _file.lower().endswith('pdf')]
