from datetime import datetime
from csv import DictReader
import os

from pytz import timezone

from reports.models import AmpouleAudit, VialAudit


class CSVToAuditLogBase(object):
    model_class = None

    def import_directory(self, directory):
        csv_files = [
            f'{directory}/{_file}' for _file in os.listdir(directory) if
            _file.lower().endswith('csv')
        ]
        for csv_file in csv_files:
            self.import_file(csv_file)

    def import_file(self, file_path):
        with open(file_path, 'r') as f:
            reader = DictReader(f, fieldnames=self.get_field_names())
            # skip header line
            next(reader)
            for line in reader:
                try:
                    self.create_from_line(line)
                except Exception as e:
                    print(f"Failed to parse line number: {reader.line_num} on file: {file_path} "
                          f"Exception: {e}. Data: {line}")

    def get_field_names(self):
        fields = self.model_class._meta.get_fields()
        return [field.name for field in fields if field.name != 'id']

    def create_from_line(self, line):
        dt = datetime.strptime(line['time_stamp'], '%d/%m/%Y %H:%M:%S').replace(tzinfo=timezone('Europe/London'))
        line['time_stamp'] = dt
        line['record_id'] = int(line['record_id'])
        object, created = self.model_class.objects.get_or_create(**line)
        if not created:
            object.save()


class AmpouleAuditImporter(CSVToAuditLogBase):
    model_class = AmpouleAudit


class VialAuditImporter(CSVToAuditLogBase):
    model_class = VialAudit
