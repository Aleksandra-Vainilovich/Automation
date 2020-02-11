import os
import shutil
import fnmatch
import glob
import sqlite3
import logging
from sqlalchemy import create_engine
from sqlalchemy import MetaData
from sqlalchemy import Table
from sqlalchemy import inspect
from sqlalchemy import Column, String, Integer

logging.basicConfig(filename = 'logging.log', format='%(asctime)s - %(message)s', level = logging.INFO, datefmt='%d-%b-%y %H:%M:%S')
logging.info('Logging configuration for new run is created')

print('move files with incorrect format')
files = os.listdir('C:\\Automation\\Input')
print(files)
for new_file in files:
    if not fnmatch.fnmatch(new_file, '*.fb2'):
        shutil.move(new_file,'C:\Automation\Incorrect_input')
        logging.info('Wrong format files are removed from the folder')

print('read all files in folder')
file_names = os.listdir('C:\Automation\Input')
print(file_names)
pth = 'C:\Automation\Input\*.fb2'
nms = glob.glob(pth)
print(nms)

conn = sqlite3.connect('C:\Automation\Automation.db')  # establishing a SQLite connection from Python
c = conn.cursor()  # Cursor object creation
print('Successfully Connected to SQLite')
logging.info('Successfully connected to SQLite')

print('Create table common for all files')
def create_table():
    try:
        c.execute('CREATE TABLE IF NOT EXISTS for_all_files '
              '( '
              'book_name TEXT'
              ', number_of_paragraph INTEGER'
              ', number_of_words INTEGER'
              ', number_of_letters INTEGER'
              ', words_with_capital_letters INTEGER'
              ', words_in_lower_case INTEGER'
              ')')
        logging.info('Table for_all_files is created')
    except Exception as error:
        logging.exception(error)
        print('ERROR', error)

create_table()

print('Insert into table common for all files')
def insertVariableIntoTable():
    try:
        for values in nms:
            if fnmatch.fnmatch(values, '*.fb2'):
                op_file = open(values, encoding="utf8")
                data_to_read = op_file.read()
                #book_name
                start = '<book-title>'
                end = '</book-title>'
                book_nm = (data_to_read.split(start))[1].split(end)[0]
                #number_of_paragraph
                paragraphs = data_to_read.split("</p>")
                count_paragraphs = len(paragraphs)
                #number_of_words
                words = data_to_read.split(" ")
                count_words = len(words)
                #number_of_letters
                count_letters = len(data_to_read)
                #words_with_capital_letters
                w_w_capital = sum(1 for cnt_upper in words if cnt_upper.isupper())
                #words_in_lowercase
                lower_cs = sum(1 for cnt_lower in words if cnt_lower.islower())
                SQLite_insert_with_param = """INSERT INTO for_all_files (book_name, number_of_paragraph, number_of_words, number_of_letters, words_with_capital_letters, words_in_lower_case)
                         VALUES (?,?,?,?,?,?)"""
                data_tuple = (book_nm, count_paragraphs, count_words, count_letters, w_w_capital, lower_cs)
                print(data_tuple)
                c.execute(SQLite_insert_with_param, data_tuple)
                conn.commit()
                print("Python Variables inserted successfully into for_all_files table")
                print(u"current directory: %s" % os.getcwd())
                logging.info('Python Variables inserted successfully into for_all_files table')
    except Exception as error:
        logging.exception(error)
        print('ERROR', error)

insertVariableIntoTable()

print('Multiple tables creation')
engine = create_engine('sqlite:///C:\Automation\Automation.db')
metadata = MetaData()
metadata.reflect(bind=engine)

def create_multiple_tables(table_name, metadata):
    tables = metadata.tables.keys()
    try:
        if table_name not in tables:
            table = Table(table_name, metadata,
                      Column('word', String),
                      Column('count', Integer),
                      Column('uppercase', Integer))
            table.create(engine)
            logging.info('The SQLite multiple tables "' + table_name + '" are created')
        for file_frequency_word_count in nms:
            if fnmatch.fnmatch(file_frequency_word_count, '*.fb2'):
                op_file = open(file_frequency_word_count, encoding="utf8")
                data_to_read = op_file.read()
                words = data_to_read.split(" ")
                for word in words:
                    SQLite_insert_many = 'INSERT INTO "' + table_name + '" VALUES (?,?,?)'
                    data_tuple = (word, words.count(word), sum(1 for cnt_upper in word if cnt_upper.isupper()))     #words frequency count, count letters in uppercase for th word
                    c.execute(SQLite_insert_many, data_tuple)
                    conn.commit()
    except Exception as error:
        logging.exception(error)
        print('ERROR', error)

tables = file_names

for tbl in tables:
    create_multiple_tables(tbl, metadata)

inspector = inspect(engine)
print(inspector.get_table_names())

conn.close()
print("The SQLite connection is closed")
logging.info('The SQLite connection is closed')


