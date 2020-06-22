import pdftotext
import psycopg2
import re
import sys
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
        username = re.sub(r"\s+", "", username, flags=re.UNICODE)
        return username.split('User:')[1].strip()

    def fetch_product_id(self, pdf):
        page = pdf[0]
        product_id = page.split('\n')[2]
        product_id = " ".join(re.split("\s+", product_id, flags=re.UNICODE))
        return product_id.split('Product:')[1].strip()

    def fetch_recipe(self, pdf):
        page = pdf[0]
        recipe = page.split('\n')[2]
        recipe = " ".join(re.split("\s+", recipe, flags=re.UNICODE))
        return recipe.split('Product:')[1].strip()

    def fetch_batch(self, pdf):
        page = pdf[0]
        batch = page.split('\n')[3]
        return batch.split('Batch:')[1].strip()

    def fetch_start_date(self, pdf):
        page = pdf[0]
        start_date = page.split('\n')[7]
        start_date = " ".join(re.split("\s+", start_date, flags=re.UNICODE))
        return start_date.split('Starting date:')[1].strip()

    def fetch_end_date(self, pdf):
        page = pdf[0]
        end_date = page.split('\n')[8]
        pattern = re.compile(r'\s+')
        end_date = " ".join(re.split("\s+", end_date, flags=re.UNICODE))
        return end_date.split('Ending date:')[1].strip()

    def fetch_inspected(self, pdf):
        page = pdf[0]
        inspected = page.split('\n')[10]
        return inspected.split('INSPECTED')[1].strip()

    def fetch_accepted(self, pdf):
        page = pdf[0]
        accepted = page.split('\n')[11]
        accepted = " ".join(re.split("\s+", accepted, flags=re.UNICODE))
        return accepted.split('ACCEPTED')[1].strip()

    def fetch_rejected(self, pdf):
        page = pdf[0]
        rejected = page.split('\n')[12]
        rejected = " ".join(re.split("\s+", rejected, flags=re.UNICODE))
        return rejected.split('REJECTED')[1].strip()

    def fetch_technical_rejects(self, pdf):
        page = pdf[0]
        technical_rejects = page.split('\n')[13]
        technical_rejects = " ".join(re.split("\s+", technical_rejects, flags=re.UNICODE))
        if sys.argv[3] == 'vials':
        	return technical_rejects.split('TECHNICAL REJECT')[1].strip()
        else:
        	return technical_rejects.split('TECNICAL REJECT')[1].strip()
