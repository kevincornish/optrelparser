import csv


class CSVToDict(object):

    def convert(self, file_name):
        results = {}
        csv = self.get_csv(file_name)
        return results

    def get_csv(self, file_name):
        with open(file_name, "r") as f:
            csv = csv.reader(f)
            next(csv)
            return csv
