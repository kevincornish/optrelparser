from datetime import datetime
from csv import DictReader, DictWriter
import os

from pytz import timezone

from reports.models import AmpouleAudit, VialAudit


class IncompleteDataError(Exception):
    pass


class CSVToAuditLogBase(object):
    model_class = None

    def import_directory(self, directory, error_log_path):
        csv_files = self.get_csv_files(directory)
        with open(error_log_path, 'w') as error_log:
            writer = DictWriter(error_log, fieldnames=['file_name', 'line_number', 'exception', 'data'])
            writer.writeheader()
            for csv_file in csv_files:
                errors = self.import_file(csv_file)
                if errors:
                    writer.writerows(errors)

    def get_csv_files(self, directory):
        return [
            f'{directory}/{_file}' for _file in os.listdir(directory) if
            _file.lower().endswith('csv')
        ]

    def import_file(self, file_path):
        try:
            return self._import_file(file_path)
        except IncompleteDataError:
            try:
                return self._import_file(file_path, delimiter=';')
            except Exception as e:
                return [{'file_name': file_path, 'line_number': 'ALL', 'exception': e, 'data': None}]
        except Exception as e:
            return [{'file_name': file_path, 'line_number': 'ALL', 'exception': e, 'data': None}]

    def _import_file(self, file_path, read_mode='r', delimiter=','):
        errors = []
        with open(file_path, read_mode, encoding='utf-8') as f:
            reader = DictReader(f, fieldnames=self.get_field_names(), delimiter=delimiter)
            # skip header line
            next(reader)
            for line in reader:
                try:
                    # If no values are found, the delimiter is most likely a semi colon. So raise an exception
                    # and try to import that way
                    if not any([line['time_stamp'], line['delta_to_utc'], line['user_id'], line['object_id']]):
                        raise IncompleteDataError(line)
                    if '$RT_COUNT$' in line['record_id']:
                        # don't process
                        continue
                    line = self.format_line(line)
                    self.create_from_line(line)
                except (KeyError, ValueError, TypeError) as e:
                    errors.append({
                        'file_name': file_path,
                        'line_number': reader.line_num,
                        'exception': e,
                        'data': line})
        return errors

    def get_field_names(self):
        fields = self.model_class._meta.get_fields()
        return [field.name for field in fields if field.name != 'id']

    def format_line(self, line):
        dt = datetime.strptime(line['time_stamp'], '%d/%m/%Y %H:%M:%S').replace(tzinfo=timezone('Europe/London'))
        line['time_stamp'] = dt
        line['record_id'] = int(line['record_id'])
        return line

    def create_from_line(self, line):
        obj, created = self.model_class.objects.get_or_create(**line)
        if not created:
            obj.save()


class BulkCSVToAuditLogBase(CSVToAuditLogBase):
    def _import_file(self, file_path, read_mode='r', delimiter=','):
        errors = []
        records = []

        with open(file_path, read_mode, encoding='utf-8') as f:
            reader = DictReader(f, fieldnames=self.get_field_names(), delimiter=delimiter)
            # skip header line
            next(reader)
            for line in reader:
                try:
                    # If no values are found, the delimiter is most likely a semi colon. So raise an exception
                    # and try to import that way
                    if not any([line['time_stamp'], line['delta_to_utc'], line['user_id'], line['object_id']]):
                        raise IncompleteDataError(line)
                    if '$RT_COUNT$' in line['record_id']:
                        # don't process
                        continue
                    line = self.format_line(line)
                    records.append()
                except (KeyError, ValueError, TypeError) as e:
                    errors.append({
                        'file_name': file_path,
                        'line_number': reader.line_num,
                        'exception': e,
                        'data': line})
        self.bulk_insert(records)
        return errors

    def bulk_insert(self, records):
        self.model_class.objects.bulk_create([self.model_class(**r) for r in records])


class AmpouleAuditImporter(CSVToAuditLogBase):
    model_class = AmpouleAudit


class BulkAmpouleAuditImporter(BulkCSVToAuditLogBase):
    model_class = AmpouleAudit


class VialAuditImporter(CSVToAuditLogBase):
    model_class = VialAudit


class BulkVialAuditImporter(BulkCSVToAuditLogBase):
    model_class = VialAudit
