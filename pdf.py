import pdftotext
import psycopg2
from config import config
from db import insert_vials, insert_ampoules

class PDFToDict(object):

    def convert(self, file_name):
        results = {}
        pdf = self.get_pdf(file_name)
        results['username'] = self.fetch_username(pdf)
        results['product_id'] = self.fetch_product_id(pdf)
        results['recipe'] = self.fetch_recipe(pdf)
        results['batch'] = self.fetch_batch(pdf)
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
        username = page.split('\n')[1]
        return username.split('User:')[1].strip()

    def fetch_product_id(self, pdf):
        page = pdf[0]
        product_id = page.split('\n')[2]
        return product_id.split('Product:')[1].strip()

    def fetch_recipe(self, pdf):
        page = pdf[0]
        recipe = page.split('\n')[2]
        return recipe.split('Product:')[1].strip()

    def fetch_batch(self, pdf):
        page = pdf[0]
        batch = page.split('\n')[3]
        return batch.split('Batch:')[1].strip()

    def fetch_start_date(self, pdf):
        page = pdf[0]
        start_date = page.split('\n')[7]
        return start_date.split('Starting date:')[1].strip()

    def fetch_end_date(self, pdf):
        page = pdf[0]
        end_date = page.split('\n')[8]
        return end_date.split('Ending date:')[1].strip()

    def fetch_inspected(self, pdf):
        page = pdf[0]
        inspected = page.split('\n')[10]
        return inspected.split('INSPECTED')[1].strip()
        
    def fetch_accepted(self, pdf):
        page = pdf[0]
        accepted = page.split('\n')[11]
        return accepted.split('ACCEPTED')[1].strip()

    def fetch_rejected(self, pdf):
        page = pdf[0]
        rejected = page.split('\n')[12]
        return rejected.split('REJECTED')[1].strip()

    def fetch_technical_rejects(self, pdf):
        page = pdf[0]
        technical_rejects = page.split('\n')[13]
        return technical_rejects.split('TECHNICAL REJECT')[1].strip()
