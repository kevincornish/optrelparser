import os

from django.core.management.base import BaseCommand

from reports.models import Ampoule
from reports.importers.report import AmpouleImporter


class Command(BaseCommand):
    def handle(self, *args, **options):
        if options['truncate']:
            Ampoule.objects.all().delete()
        processor = AmpouleImporter()
        processor.import_directory(options['directory'])

    def add_arguments(self, parser):
        parser.add_argument("-d", "--dir", action="store", dest="directory", type=str, default='files/ampoules')
        parser.add_argument(
            "-o", "--output", action="store", dest="ampoules_import", type=str, default='logs/ampoules_import.csv')
        parser.add_argument("--truncate", action="store_true", dest="truncate", default=False)
        return parser

    def get_pdfs(self, directory):
        return [f'{directory}/{_file}' for _file in os.listdir(directory) if
                _file.lower().endswith('pdf')]
