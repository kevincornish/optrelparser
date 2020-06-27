import os

from reports.models import Ampoule, Vial
from reports.pdf_parser import PDFToDict


class CSVToAuditLogBase(object):
    model_class = None

    def import_directory(self, directory):
        pdfs = self.get_pdfs(directory)
        converter = PDFToDict()
        for pdf in pdfs:
            try:
                data = converter.convert(pdf)
                if data['inspected'] == '0':
                    # don't process
                    continue
                object, created = self.model_class.objects.get_or_create(**data)
                if not created:
                    object.save()
            except Exception as e:
                print(pdf, e)

    def get_pdfs(self, directory):
        return [f'{directory}/{_file}' for _file in os.listdir(directory) if
                _file.lower().endswith('pdf')]


class AmpouleImporter(CSVToAuditLogBase):
    model_class = Ampoule


class VialImporter(CSVToAuditLogBase):
    model_class = Vial
