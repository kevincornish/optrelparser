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

            #data['username'] = username
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

