import os
from reports.models import VialAudit
from postgres_copy import CopyMapping
from django.core.management.base import BaseCommand

class Command(BaseCommand):
    def handle(self, *args, **options):
        csvs = self.get_csvs(options['directory'])
        for csv in csvs:
                c = CopyMapping(VialAudit,csv, dict(RecordID='RecordID', TimeStamp='TimeStamp', DeltaToUTC='DeltaToUTC', UserID='UserID', ObjectID='ObjectID', Description='Description', Comment='Comment', Checksum='Checksum'))
#                if c['RecordID'] == '$RT_COUNT$':
#                        # don't process
#                        continue
                c.save()

    def add_arguments(self, parser):
        parser.add_argument("-d", "--dir", action="store", dest="directory", type=str, default='files/vial_audit')
        return parser

    def get_csvs(self, directory):
        return [f'{directory}/{_file}' for _file in os.listdir(directory) if
                _file.lower().endswith('csv')]
