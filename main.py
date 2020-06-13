import os
import sqlalchemy as db
import pdftotext
#connect to db
engine = db.create_engine('sqlite:///reports.sqlite')
connection = engine.connect()
metadata = db.MetaData()
#load the tables
vials = db.Table('vials', metadata, autoload=True, autoload_with=engine)
ampoules = db.Table('ampoules', metadata, autoload=True, autoload_with=engine)
class ProcessPDFs(object):
	def process(self, directory):
		pdfs = self.get_pdfs(directory)
		converter = PDFToDict()
		# iterate through the directory
		for pdf in pdfs:
			data = converter.convert(pdf)
			# do something with data    
	def get_pdfs(self, directory):
		return [f'{directory}/{file}' for file in os.listdir(directory) if file.lower().endswith('pdf')]

class PDFToDict(object):    
	def convert(self, file_name):
        	results = {}
        	pdf = self.get_pdf(file_name)
        	results['product_id'] = self.fetch_product_id(pdf)
        	results['recipe_id'] = self.fetch_recipe_id(pdf)
        	# add more here
        	return results    

	def get_pdf(self, file_name):
        # open PDF
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
	query = db.insert(vials).values(id=1, product='test', recipe=1) 
	#this needs to store the data fetched
	insert = connection.execute(query)   
