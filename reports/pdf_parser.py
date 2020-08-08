import re
from datetime import datetime

from pytz import timezone
import pdftotext


class PDFToDict(object):

    def convert(self, file_name):
        results = {}
        pdf = self.get_pdf(file_name)
        results['username'] = self.fetch_username(pdf)
        results['product_id'] = self.fetch_product_id(pdf)
        results['recipe'] = self.fetch_recipe(pdf)
        results['batch_name'] = self.fetch_batch_name(pdf)
        results['batch_number'] = self.fetch_batch_number(pdf)
        results['start_date'] = self.fetch_start_date(pdf)
        results['end_date'] = self.fetch_end_date(pdf)
        results['inspected'] = self.fetch_inspected(pdf)
        results['accepted'] = self.fetch_accepted(pdf)
        results['rejected'] = self.fetch_rejected(pdf)
        results['technical_rejects'] = self.fetch_technical_rejects(pdf)
        return results

    def get_pdf(self, file_name):
        with open(file_name, "rb") as f:
            pdf = pdftotext.PDF(f)
            return pdf

    def fetch_username(self, pdf):
        page = pdf[0]
        username = page.split('User:')[1].split('\n')[0].strip().split(' ')[-1]
        return username

    def fetch_product_id(self, pdf):
        page = pdf[0]
        return page.split('Product:')[1].split('\n')[0].strip().split()[0]

    def fetch_recipe(self, pdf):
        page = pdf[0]
        product_line_with_rest_of_page = page.split('Product:')[1]
        product_line = product_line_with_rest_of_page.split('\n')[0]
        cleaned_product_line = product_line.strip()
        product_id_and_recipe = cleaned_product_line.split()
        # ignore product id (first element in list)
        recipe = ' '.join(product_id_and_recipe[1:])
        return recipe

## TO FIX:
## If batch name includes strength it is stripped
## Replace char.isdigit to
## only strip number regex [0-9]{7,8}
    def fetch_batch_name(self, pdf):
        page = pdf[0]
        line = page.split('Batch:')[-1].split('\n')[0].strip()
        return ''.join([char for char in line if not char.isdigit()]).strip()

    def fetch_batch_number(self, pdf):
        page = pdf[0]
        try:
            result = re.findall(r"[0-9]{7,8}", page)[-1]
            if result == '21490035':
                result = None
            if result == '21490030':
                result = None
            return result
        except IndexError:
            return None

    def fetch_start_date(self, pdf):
        page = pdf[0]
        full_string = page.split("Starting date:")[-1].split('\n')[0].strip().split()
        return self.convert_time(full_string)

    def fetch_end_date(self, pdf):
        page = pdf[0]
        full_string = page.split("Ending date:")[-1].split('\n')[0].strip().split()
        return self.convert_time(full_string)
###TODO: date is storing m/d/y
##Also rounding times from 13:14:18 to 13:15
##also mixing am and pm up
##10/12/2017 4:05 a.m should be 12/10/2017 4:04:12 PM
    def convert_time(self, string):
        try:
            dt = self.convert_time_12_hr(string)
        except:
            dt = self.convert_time_24_hr(string)
        return dt.replace(tzinfo=timezone('Europe/London'))

    def convert_time_12_hr(self, string):
        date = string[0]
        time = string[1]
        am_or_pm = string[2]
        dt = f'{date} {time} {am_or_pm}'
        return datetime.strptime(dt, '%d/%m/%Y %H:%M:%S %p')

    def convert_time_24_hr(self, string):
        date = string[0]
        time = string[-1]
        dt = f'{date} {time}'
        return datetime.strptime(dt, '%d/%m/%Y %H:%M:%S')

    def fetch_inspected(self, pdf):
        page = pdf[0]
        return page.split('INSPECTED')[1].split('\n')[0].strip()

    def fetch_accepted(self, pdf):
        page = pdf[0]
        return page.split('ACCEPTED')[1].split('\n')[0].split()[0]

    def fetch_rejected(self, pdf):
        page = pdf[0]
        return page.split('REJECTED')[1].split('\n')[0].split()[0]

    def fetch_technical_rejects(self, pdf):
        page = pdf[0]
        try:
            return page.split('TECHNICAL REJECT')[1].split('\n')[0].split()[0]
        except:
            return page.split('TECNICAL REJECT')[1].split('\n')[0].split()[0]
