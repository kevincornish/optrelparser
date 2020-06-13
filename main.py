import os
import argparse

from db import insert_vials_from_dict
from pdf import PDFToDict


class ProcessPDFs(object):
	def process(self, directory):
		pdfs = self.get_pdfs(directory)
		converter = PDFToDict()
		for idx, pdf in enumerate(pdfs):
			data = converter.convert(pdf)
			# You want to fetch the highest ID from the table or truncate it
			# to get an actual ID.
			data['id'] = idx
			insert_vials_from_dict(data)

	def get_pdfs(self, directory):
		return [f'{directory}/{_file}' for _file in os.listdir(directory) if
				_file.lower().endswith('pdf')]

if __name__ == '__main__':
	parser = argparse.ArgumentParser(description='Process some integers.')
	parser.add_argument('-d', dest='directory', type=str,
						help='the directory of pdfs to parse')

	args = parser.parse_args()
	processor = ProcessPDFs()
	processor.process(args.directory)

