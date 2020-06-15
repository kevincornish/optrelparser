import pdftotext
import psycopg2
from config import config
from db import insert_vials

class PDFToDict(object):

    def convert(self, file_name):
        results = {}
        pdf = self.get_pdf(file_name)
        results['username'] = self.fetch_username(pdf)
        results['product_id'] = self.fetch_product_id(pdf)
        #results['recipe'] = self.fetch_recipe(pdf)
        results['batch'] = self.fetch_batch(pdf)
        #results['start_date'] = self.fetch_start_date(pdf)
        #results['end_date'] = self.fetch_end_date(pdf)
        #results['inspected'] = self.fetch_inspected(pdf)
        #results['accepted'] = self.fetch_accepted(pdf)
        #results['rejected'] = self.fetch_rejected(pdf)
        #results['technical_rejects'] = self.fetch_technical_rejects(pdf)
        return results

    def get_pdf(self, file_name):
        with open(file_name, "rb") as f:
            pdf = pdftotext.PDF(f)
            return pdf

    def fetch_username(self, pdf):
        page = pdf[0]
        line = page.split('\n')[1]
        print (line)        
        #return line.split('User:')[1].strip()

    def fetch_product_id(self, pdf):
        page = pdf[0]
        line = page.split('\n')[2]
        print (line)
        #return line.split('Product ID:')[1].strip()

    def fetch_batch(self, pdf):
        page = pdf[0]
        line = page.split('\n')[3]
        print (line)
        #return line.split('Batch:')[1].strip()

