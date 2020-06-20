import os
import argparse

from db import insert_vials
from pdf import PDFToDict


class ProcessPDFs(object):
    def process(self, directory):
        pdfs = self.get_pdfs(directory)
        converter = PDFToDict()
        for idx, pdf in enumerate(pdfs):
            data = converter.convert(pdf)

            data['username'] = username
            data['product_id'] = product_id
            data['recipe'] = recipe
            data['batch'] = batch
            data['start_date'] = start_date
            data['end_date'] = end_date
            data['inspected'] = inspected
            data['accepted'] = accepted
            data['rejected'] = rejected
            data['technical_rejects'] = technical_rejects
            insert_vials(data)
            #insert_vials([(fetch_username,fetch_product_id,fetch_recipe,fetch_batch,fetch_start_date,fetch_end_date, fetch_inspected,fetch_accepted,fetch_rejected,fetch_technical_rejects)])

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

