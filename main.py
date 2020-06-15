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
            # You want to fetch the highest ID from the table or truncate it
            # to get an actual ID.
            #data['id'] = idx
            #insert_vials(data)

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

    #insert_vials([
   #     ('1','Kev','3','50mL Production','12345678 Morphine Sulfate','01/01/2020 09:30am','02/01/2020 10:31am', '100','90','10','0',),
   #     ('2','Billy','4','100mL Production','12345679 Morphine Sulfate','02/01/2020 11:50am','04/01/2020 12:12pm', '1000','900','100','0',)
   # ])

