from django.core.management.base import BaseCommand

from reports.importers.audit_log import AmpouleAuditImporter


class Command(BaseCommand):
    def handle(self, *args, **options):
        processor = AmpouleAuditImporter()
        processor.import_directory(options['directory'])

    def add_arguments(self, parser):
        parser.add_argument("-d", "--dir", action="store", dest="directory", type=str, default='files/ampoule_audit')
        return parser
