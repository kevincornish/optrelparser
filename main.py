import os
from db import insert_vials, insert_ampoules
from pdf import PDFToDict
from setup import create_tables
from search import search_vials, search_ampoules


class ProcessPDFs(object):
    def process(self, directory):
        pdfs = self.get_pdfs(directory)
        converter = PDFToDict()
        for idx, pdf in enumerate(pdfs):
            data = converter.convert(pdf)
            if directoryinp == 'vials':
            	insert_vials(data)
            else:
            	insert_ampoules(data)
            #print (data['username'])

    def get_pdfs(self, directory):
        return [f'{directory}/{_file}' for _file in os.listdir(directory) if
                _file.lower().endswith('pdf')]


if __name__ == '__main__':

    setup = input("Do you want to create tables in db? y/n >>> ")
    setupBool = False
    if setup == 'y':
        setupBool = True
    else:
        setupBool = False

    if setupBool == True:
        create_tables()

    importing = input("Do you want to import pdfs to db? y/n >>> ")
    importingBool = False
    if importing == 'y':
        importingBool = True
    else:
        importingBool = False

    if importingBool == True:
        directoryinp = input("vials or ampoules >>> ")
        processor = ProcessPDFs()
        processor.process(directoryinp)

    search = input("Would you like to search for a batch? y/n >>> ")
    searchBool = False
    if search == 'y':
        searchBool = True
    else:
        searchBool = False

    if searchBool == True:
        searchinp = input("vials or ampoules >>> ")
        if searchinp == 'vials':
            search_vials()
        if searchinp == 'ampoules':
            search_ampoules()
