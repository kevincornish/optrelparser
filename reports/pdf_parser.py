import re
import pdftotext
from datetime import datetime


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
        return ' '.join(page.split('Product:')[1].split('\n')[0].strip().split()[1:])

    def fetch_batch_name(self, pdf):
        page = pdf[0]
        line = page.split('Batch:')[-1].split('\n')[0].strip()
        return ''.join([char for char in line if not char.isdigit()]).strip()

    def fetch_batch_number(self, pdf):
        page = pdf[0]
        line = page.split('Batch:')[-1].split('\n')[0].strip()
        expr = re.compile('\d+')
        try:
            return re.findall(expr, line)[0]
        except IndexError:
            return None

    def fetch_start_date(self, pdf):
        page = pdf[0]
        full_string = page.split("Starting date:")[-1].split('\n')[0].strip().split()
        date = full_string[0]
        time = full_string[-1]
        dt = f'{date} {time}'
        return datetime.strptime(dt, '%d/%m/%Y %H:%M:%S')

    def fetch_end_date(self, pdf):
        page = pdf[0]
        full_string = page.split("Ending date:")[-1].split('\n')[0].strip().split()
        date = full_string[0]
        time = full_string[-1]
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
