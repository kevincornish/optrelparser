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

    def fetch_product_id(self, pdf):
        # Because I hate regex, this is the ghetto way. The more appropriate was
        # is definitely to use regex
        page = pdf[0]
        # 'Product ID:     T8715N_EPISTATUS          Recipe ID:           T8715N_EPISTATUS'
        line = page.split('\n')[5]
        # split the line on the text you know:
        # split on Product ID:, grab the second element.
        # split on Recipe ID:, grab the first element and trim the whitespace
        return line.split('Product ID:')[1].split('Recipe ID')[0].strip()

    def fetch_recipe_id(self, pdf):
        page = pdf[0]
        # 'Product ID:     T8715N_EPISTATUS          Recipe ID:           T8715N_EPISTATUS'
        line = page.split('\n')[5]
        return line.split('Recipe ID:')[1].strip()

if __name__ == '__main__':
    insert_vials([
        ('1','Kev','3','50mL Production','12345678 Morphine Sulfate','01/01/2020 09:30am','02/01/2020 10:31am', '100','90','10','0',),
        ('2','Billy','4','100mL Production','12345679 Morphine Sulfate','02/01/2020 11:50am','04/01/2020 12:12pm', '1000','900','100','0',)
    ])
