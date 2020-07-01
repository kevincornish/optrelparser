from django.core.management.base import BaseCommand

from reports.models import VialAudit
from reports.importers.audit_log import BulkVialAuditImporter, VialAuditImporter


class Command(BaseCommand):
    def handle(self, *args, **options):
        if options['truncate']:
            VialAudit.objects.all().delete()
            processor = BulkVialAuditImporter()
        else:
            processor = VialAuditImporter()

        processor.import_directory(options['directory'], options['audit_log'])

    def add_arguments(self, parser):
        parser.add_argument("-d", "--dir", action="store", dest="directory", type=str, default='files/vial_audit')
        parser.add_argument(
            "-o", "--output", action="store", dest="audit_log", type=str, default='logs/vial_audit.csv')
        parser.add_argument(
            "--truncate", action="store_true", dest="truncate", default=False)
        return parser
