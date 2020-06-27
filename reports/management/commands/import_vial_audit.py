from django.core.management.base import BaseCommand

from reports.importers.audit_log import VialAuditImporter


class Command(BaseCommand):
    def handle(self, *args, **options):
        processor = VialAuditImporter()
        processor.import_directory(options['directory'])

    def add_arguments(self, parser):
        parser.add_argument("-d", "--dir", action="store", dest="directory", type=str, default='files/vial_audit')
        return parser
