from lxml import html
import codecs
import os
import sqlalchemy as db
#connect to db
engine = db.create_engine('sqlite:///reports.sqlite')
connection = engine.connect()
metadata = db.MetaData()
#load the tables
vials = db.Table('vials', metadata, autoload=True, autoload_with=engine)
amps = db.Table('ampoules', metadata, autoload=True, autoload_with=engine)


# ask if user wants to convert pdfs
# if yes convert the pdf to text/html
#os.system("pdf2txt -o output.html *.pdf")

# open file
#file = codecs.open("output.html", "r", "utf-8")
#data = file.read()
#html_file = html.fromstring(data)
# get the text from <div><span>text</span><div>
#extracted_data = html_file.xpath('//div//span/text()')
# return array of elements
#for elm in extracted_data:
#    line_elements = elm.split()
#    print(line_elements)
#file.close();
