import os

from django.core.management.base import BaseCommand

from reports.pdf_parser import PDFToDict
from reports.models import Ampoule


class Command(BaseCommand):
    def handle(self, *args, **options):
        pdfs = self.get_pdfs(options['directory'])
        converter = PDFToDict()
        for pdf in pdfs:
            data = converter.convert(pdf)
            if data['inspected'] == '0':
            	# don't process
            	continue
            ampoule = Ampoule(**data)
            ampoule.save()

    def add_arguments(self, parser):
        parser.add_argument("-d", "--dir", action="store", dest="directory", type=str, default='files/ampoules')
        return parser

    def get_pdfs(self, directory):
        return [f'{directory}/{_file}' for _file in os.listdir(directory) if
                _file.lower().endswith('pdf')]
