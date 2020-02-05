

import os
import shutil
import fnmatch
import glob
import sqlite3
import logging
import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy import MetaData
from sqlalchemy import Table
from sqlalchemy import inspect
from sqlalchemy import Column, String, Integer
from collections import Counter
from sqlalchemy.engine.url import URL

#, re, errno, sys
#os.chdir('c:\Automation\Input')
# from Create_table import create_table
from sqlalchemy.util import counter

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

print('book title')
for files_to_read_titles in nms:
    if fnmatch.fnmatch(files_to_read_titles, '*.fb2'):
        op_file = open(files_to_read_titles, encoding="utf8")
        data_to_read = op_file.read()
        start = '<book-title>'
        end = '</book-title>'
        #print((data_to_read.split(start))[1].split(end)[0])
        #text_title = ((data_to_read.split(start))[1].split(end)[0]) #class STRING
        #text_title = [((data_to_read.split(start))[1].split(end)[0])]  # class LIST
        text_title = (data_to_read.split(start))[1].split(end)[0]  #class STRING
        print(text_title)
print(type(text_title))

print('all files words count')
for file_word_count in nms:
    op_file = open(file_word_count, encoding="utf8")
    data_to_read = op_file.read()
    words = data_to_read.split(" ")
    count_words = len(words)
    start = '<book-title>'
    end = '</book-title>'
    print((data_to_read.split(start))[1].split(end)[0], ': count of words', count_words)
    print(count_words)
    print(type(count_words))
print(count_words)
print(type(count_words))
# for file_word_count_real in nms:
#     op_file = open(file_word_count_real, encoding="utf8")
#     data_to_read = op_file.read()
#     words = data_to_read.split(" ")
#     count_words = len(words)
#     print(count_words)

print('ddddddddddddddd')
def file_word_count_int():
    for file_word_count_real in nms:
        op_file = open(file_word_count_real, encoding="utf8")
        data_to_read = op_file.read()
        words = data_to_read.split(" ")
        count_words = len(words)
        print(type(count_words))
        print(count_words)
        #return len(words)

file_word_count_int()
print('fgfgfgfgfgfgfgfgfgfgfgfgf')
fgfg = file_word_count_int()
print(fgfg)
print(type(fgfg))

print('number_of_paragraph')
for number_of_paragraph in nms:
    if fnmatch.fnmatch(number_of_paragraph, '*.fb2'):
        op_file = open(number_of_paragraph, encoding="utf8")
        data_to_read = op_file.read()
        paragraphs = data_to_read.split("</p>")
        count_paragraphs = len(paragraphs)
        start = '<book-title>'
        end = '</book-title>'
        a=((data_to_read.split(start))[1].split(end)[0], ': count of paragraphs',count_paragraphs)
        paragraph_count=count_paragraphs
print(count_paragraphs)
# for number_of_paragraph_real in nms:
#     if fnmatch.fnmatch(number_of_paragraph_real, '*.fb2'):
#         op_file = open(number_of_paragraph_real, encoding="utf8")
#         data_to_read = op_file.read()
#         paragraphs = data_to_read.split("</p>")
#         count_paragraphs = len(paragraphs)
#         print(count_paragraphs)

# print('gggggggggggggggggggggg')
# def number_of_paragraph_int():
#     for number_of_paragraph_real in nms:
#         if fnmatch.fnmatch(number_of_paragraph_real, '*.fb2'):
#             op_file = open(number_of_paragraph_real, encoding="utf8")
#             data_to_read = op_file.read()
#             paragraphs = data_to_read.split("</p>")
#             count_paragraphs = len(paragraphs)
#             print(count_paragraphs)
#
# number_of_paragraph_int()

print('number_of_letters')
for number_of_letters in nms:
    if fnmatch.fnmatch(number_of_letters, '*.fb2'):
        op_file = open(number_of_letters, encoding="utf8")
        data_to_read = op_file.read()
        count_letters = len(data_to_read)
        start = '<book-title>'
        end = '</book-title>'
        print((data_to_read.split(start))[1].split(end)[0], ': count of letters', count_letters)
# for number_of_letters_real in nms:
#     if fnmatch.fnmatch(number_of_letters_real, '*.fb2'):
#         op_file = open(number_of_letters_real, encoding="utf8")
#         data_to_read = op_file.read()
#         count_letters = len(data_to_read)
#         print(count_letters)

# def number_of_letters_int():
#     for number_of_letters_real in nms:
#         if fnmatch.fnmatch(number_of_letters_real, '*.fb2'):
#             op_file = open(number_of_letters_real, encoding="utf8")
#             data_to_read = op_file.read()
#             count_letters = len(data_to_read)
#             print(count_letters)
#
# number_of_letters_int()

print('words with capital letters')
for words_in_file in nms:
    if fnmatch.fnmatch(words_in_file, '*.fb2'):
        op_file = open(words_in_file, encoding="utf8")
        data_to_read = op_file.read()
        words = data_to_read.split(" ")
        start = '<book-title>'
        end = '</book-title>'
        #print(data_to_read)
        print((data_to_read.split(start))[1].split(end)[0], ': words with capital letters', sum(1 for cnt_upper in words if cnt_upper.isupper()))
        #print('lower letters', sum(1 for cnt_lower in data_to_read if cnt_lower.islower()))
        words_with_capital_letters = sum(1 for cnt_upper in words if cnt_upper.isupper())
# for words_with_capital_letters_real in nms:
#     if fnmatch.fnmatch(words_with_capital_letters_real, '*.fb2'):
#         op_file = open(words_with_capital_letters_real, encoding="utf8")
#         data_to_read = op_file.read()
#         words = data_to_read.split(" ")
#         print(sum(1 for cnt_upper in words if cnt_upper.isupper()))

# def words_with_capital_letters_int():
#     for words_with_capital_letters_real in nms:
#         if fnmatch.fnmatch(words_with_capital_letters_real, '*.fb2'):
#             op_file = open(words_with_capital_letters_real, encoding="utf8")
#             data_to_read = op_file.read()
#             words = data_to_read.split(" ")
#             print(sum(1 for cnt_upper in words if cnt_upper.isupper()))
#
# words_with_capital_letters_int()

print('number of capital letters')
for words_in_file_with_capital_letters in nms:
    if fnmatch.fnmatch(words_in_file_with_capital_letters, '*.fb2'):
        op_file = open(words_in_file_with_capital_letters, encoding="utf8")
        data_to_read = op_file.read()
        start = '<book-title>'
        end = '</book-title>'
        #words = data_to_read.split(" ")
        #print(data_to_read)
        print((data_to_read.split(start))[1].split(end)[0], ': number of capital letters', sum(1 for cnt_upper in data_to_read if cnt_upper.isupper()))
        #print('lower letters', sum(1 for cnt_lower in data_to_read if cnt_lower.islower()))
        nmbr_of_capital_letters = sum(1 for cnt_upper in data_to_read if cnt_upper.isupper())

print('words in lower case')
for words_in_lower_case in nms:
    if fnmatch.fnmatch(words_in_lower_case, '*.fb2'):
        op_file = open(words_in_lower_case, encoding="utf8")
        data_to_read = op_file.read()
        words = data_to_read.split(" ")
        start = '<book-title>'
        end = '</book-title>'
        #print(data_to_read)
        print((data_to_read.split(start))[1].split(end)[0], ': words in lower case', sum(1 for cnt_lower in words if cnt_lower.islower()))
        #print('lower letters', sum(1 for cnt_lower in data_to_read if cnt_lower.islower()))
        lower_case_words = sum(1 for cnt_lower in words if cnt_lower.islower())
# for words_in_lower_case_real in nms:
#     if fnmatch.fnmatch(words_in_lower_case_real, '*.fb2'):
#         op_file = open(words_in_lower_case_real, encoding="utf8")
#         data_to_read = op_file.read()
#         words = data_to_read.split(" ")
#         print(sum(1 for cnt_lower in words if cnt_lower.islower()))
# print(words_in_lower_case_real)

# def words_in_lower_case_int():
#     for words_in_lower_case_real in nms:
#         if fnmatch.fnmatch(words_in_lower_case_real, '*.fb2'):
#             op_file = open(words_in_lower_case_real, encoding="utf8")
#             data_to_read = op_file.read()
#             words = data_to_read.split(" ")
#             print(sum(1 for cnt_lower in words if cnt_lower.islower()),'gjhj')
#
# words_in_lower_case_int()

#print(words_in_lower_case_int(), words_with_capital_letters_int(), 'hghhghhghghgh', sep=',')

# print('All values in one row')
# def values_list():
#     for values in nms:
#         if fnmatch.fnmatch(values, '*.fb2'):
#             op_file = open(values, encoding="utf8")
#             data_to_read = op_file.read()
#             #book_name
#             start = '<book-title>'
#             end = '</book-title>'
#             book_nm = (data_to_read.split(start))[1].split(end)[0]
#             #number_of_paragraph
#             paragraphs = data_to_read.split("</p>")
#             count_paragraphs = len(paragraphs)
#             #number_of_words
#             words = data_to_read.split(" ")
#             count_words = len(words)
#             #number_of_letters
#             count_letters = len(data_to_read)
#             #words_with_capital_letters
#             w_w_capital = sum(1 for cnt_upper in words if cnt_upper.isupper())
#             #words_in_lowercase
#             lower_cs = sum(1 for cnt_lower in words if cnt_lower.islower())
#             mytuple=((data_to_read.split(start))[1].split(end)[0]
#                      ,int(count_paragraphs)
#                      ,int(count_words)
#                      ,int(count_letters)
#                      ,int(sum(1 for cnt_upper in words if cnt_upper.isupper()))
#                      ,int(sum(1 for cnt_lower in words if cnt_lower.islower()))
#                      )
#             #print(mytuple,',')
#             #print(mytuple[0:6])
#             #return book_nm,count_paragraphs,count_words,count_letters,w_w_capital, lower_cs #TUPLE
#             #return [book_nm, count_paragraphs, count_words, count_letters, w_w_capital, lower_cs]  #LIST
#             return mytuple
#             #print(type(mytuple))
#
# values_list()
# print(values_list())
# val = values_list()
# print(type(val))
# #print(type(values_list()))
# print('ttttttttttttttttt')
# data_g = str(values_list())
# #print(data_g, sep=',')
# print('yyyyyyyyyyyyy')
# g = data_g.split('\n')
# print(g)
# # print('hhhhhhhhhhhhh')
# # print(data_g)
# # print('fffffffffffff')
# # print(values_list())
# # for string in data_g or []:
# #     a = string.split(',')
# #     print(a)

print('insert into table')

# conn = sqlite3.connect('Automation.db') #establishing a SQLite connection from Python
# c = conn.cursor() #Cursor object creation
# # #
# # #def data_entry():
# # #     book_name = files_to_read_titles
# # #     number_of_paragraph = number_of_paragraph_real
# # #     number_of_words = file_word_count_real
# # #     number_of_letters = number_of_letters_real
# # #     words_with_capital_letters = words_with_capital_letters_real
# # #     words_in_lower_case = words_in_lower_case_real
# # #values_to_insert = [(files_to_read_titles_text(),), (number_of_paragraph_int(),), (file_word_count_int(),), (number_of_letters_int(),), (words_with_capital_letters_int(),), (words_in_lower_case_int(),),]
# # #values_to_insert = [files_to_read_titles_text(), number_of_paragraph_int(), file_word_count_int(), number_of_letters_int(), words_with_capital_letters_int(), words_in_lower_case_int()]
# # #values_to_insert = [[files_to_read_titles_text()], [number_of_paragraph_int()], [file_word_count_int()], [number_of_letters_int()], [words_with_capital_letters_int()], [words_in_lower_case_int()]]
# # #values_to_insert = [print([files_to_read_titles_text()]), print([number_of_paragraph_int()]), print([file_word_count_int()]), print([number_of_letters_int()]), print([words_with_capital_letters_int()]), print([words_in_lower_case_int()])]
# #
# # #values_to_insert = [print([values_list()])]
# # #values_to_insert = print([values_list()])
# # print('Values list')
# # values_to_insert = values_list()
# # print(values_list())
# #
# # def table_insert():
# #     c.execute("INSERT INTO for_all_files (book_name, number_of_paragraph, number_of_words, number_of_letters, words_with_capital_letters, words_in_lower_case) VALUES (?,?,?,?,?,?)", [values_to_insert,])
# #
# #
# def table_insert():
#     c.execute("""INSERT INTO for_all_files (book_name, number_of_paragraph, number_of_words, number_of_letters, words_with_capital_letters, words_in_lower_case) VALUES
#                                     (
#                                     text_title
#                                     , paragraph_count
#                                     , count_words
#                                     , count_letters
#                                     , words_with_capital_letters
#                                     , lower_case_words
#                                     )"""
#               )
# table_insert()
#
# conn.commit() # make changes persistent in the database
# # c.rowcount # the number of rows affected.
# # # def read_from_db():
# # #     c.execute('SELECT * FROM for_all_files')
# # #     #data = c.fetchall()
# # #     #print(data)
# # #     for row in c.fetchall():
# # #         print(row)
# #
# c.close()
# conn.close() #Closing connection with the database
#  #print(values_to_insert)
#

# print('Third insert way works fine')
# def insertVariableIntoTable(book_name, number_of_paragraph, number_of_words, number_of_letters, words_with_capital_letters, words_in_lower_case):
#     try:
#         conn = sqlite3.connect('Automation.db')  # establishing a SQLite connection from Python
#         c = conn.cursor()  # Cursor object creation
#         print('Successfully Connected to SQLite')
#         logging.info('Connected to SQLite to insert into for_all_files table')
#
#         SQLite_insert_with_param = """INSERT INTO for_all_files (book_name, number_of_paragraph, number_of_words, number_of_letters, words_with_capital_letters, words_in_lower_case)
#                          VALUES (?,?,?,?,?,?)"""
#         data_tuple = (book_name, number_of_paragraph, number_of_words, number_of_letters, words_with_capital_letters, words_in_lower_case)
#         c.execute(SQLite_insert_with_param, data_tuple)
#         conn.commit()
#         print("Python Variables inserted successfully into for_all_files table")
#         logging.info('Python Variables inserted successfully into for_all_files table')
#         c.close()
#     except Exception as error: #ValueError #sqlite3.Error
#         #raise error
#         #print("Failed to insert Python variable into sqlite table", error)
#         #logging.error('Failed to insert Python variable into sqlite table', exc_info = True)
#         #logging.exception('Failed to insert Python variable into sqlite table')
#         logging.exception(error)
#         #logging.error('Error at %s', 'Failed to insert Python variable into sqlite table', exc_info=error)
#         #logging.exception('Failed to insert Python variable into sqlite table', error)
#     finally:
#         conn.close()
#         print("The SQLite connection is closed")
#         logging.info('The SQLite connection is closed')
#
# #insertVariableIntoTable(values_list())
# #insertVariableIntoTable('fgfg',675,8976,6545,6767,9609) # this one works
# #insertVariableIntoTable(tuple(('Цветы для Элджернона', 2268, 69054, 500660, 961, 55280),('Цветы для Элджернона 777', 2268, 69054, 500660, 961, 55280), ('Цветы для Элджернона 45', 2268, 69054, 500660, 961, 55280)))
#
# #insertVariableIntoTable(values_list())
# def Variable_insert():
#     try:
#         insertVariableIntoTable(text_title, paragraph_count, count_words, count_letters, words_with_capital_letters, lower_case_words)
#         #insertVariableIntoTable(print(fgfg), print(fgfg), print(fgfg), print(fgfg), print(fgfg), print(fgfg))
#         logging.info('Python Variables inserted successfully into for_all_files table')
#     except Exception as error:
#         logging.exception(error)
#
# Variable_insert()
# #
# # #insertVariableIntoTable(text_title,  paragraph_count, count_words, count_letters, words_with_capital_letters, lower_case_words)
#
# print('wwwwww')


conn = sqlite3.connect('Automation.db')  # establishing a SQLite connection from Python
c = conn.cursor()  # Cursor object creation
print('Successfully Connected to SQLite')
logging.info('Successfully connected to SQLite')

print('FOURTH insert way')
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
                # conn = sqlite3.connect('Automation.db')  # establishing a SQLite connection from Python
                # c = conn.cursor()  # Cursor object creation
                # print('Successfully Connected to SQLite')
                # logging.info('Connected to SQLite to insert into for_all_files table')

                SQLite_insert_with_param = """INSERT INTO for_all_files (book_name, number_of_paragraph, number_of_words, number_of_letters, words_with_capital_letters, words_in_lower_case)
                         VALUES (?,?,?,?,?,?)"""
                #c.execute(
                    #"INSERT INTO for_all_files (book_name, number_of_paragraph, number_of_words, number_of_letters, words_with_capital_letters, words_in_lower_case)\n"
                    #"                                         VALUES (book_nm, paragraphs, count_words, count_letters, w_w_capital, lower_cs)")
                data_tuple = (book_nm, count_paragraphs, count_words, count_letters, w_w_capital, lower_cs)
                print(data_tuple)
                c.execute(SQLite_insert_with_param, data_tuple)
                conn.commit()
                print("Python Variables inserted successfully into for_all_files table")
                logging.info('Python Variables inserted successfully into for_all_files table')
                #c.close()
    except Exception as error: #ValueError #sqlite3.Error
        #raise error
        #print("Failed to insert Python variable into sqlite table", error)
        #logging.error('Failed to insert Python variable into sqlite table', exc_info = True)
        #logging.exception('Failed to insert Python variable into sqlite table')
        logging.exception(error)
        #logging.error('Error at %s', 'Failed to insert Python variable into sqlite table', exc_info=error)
        #logging.exception('Failed to insert Python variable into sqlite table', error)
    # finally:
    #     conn.close()
    #     print("The SQLite connection is closed")
    #     logging.info('The SQLite connection is closed')

insertVariableIntoTable()

print('Multiple tables creation')

engine = create_engine('sqlite:///Automation.db')

metadata = MetaData()
metadata.reflect(bind=engine)

def create_multiple_tables(table_name, metadata):
    tables = metadata.tables.keys()
    try:
        if table_name not in tables:
        # conn = sqlite3.connect('Automation.db')  # establishing a SQLite connection from Python
        # c = conn.cursor()  # Cursor object creation
            table = Table(table_name, metadata,
                      Column('word', String),
                      Column('count', Integer),
                      Column('uppercase', Integer))
            table.create(engine)
            logging.info('The SQLite multiple tables are created')
    except Exception as error:
        logging.exception(error)
        #c.execute(SQLite_insert_with_param, data_tuple)
        #conn.commit()
        #print("Python Variables inserted successfully into for_all_files table")
        #logging.info('Python Variables inserted successfully into for_all_files table')
        #c.close()

tables = file_names
for tbl in tables:
    create_multiple_tables(tbl, metadata)

inspector = inspect(engine)
print(inspector.get_table_names())

conn.close()
print("The SQLite connection is closed")
logging.info('The SQLite connection is closed')

print('wwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwww')

print('words frequency count')
def insertVariableIntoTable():
    try:
        for file_frequency_word_count in nms:
            if fnmatch.fnmatch(file_frequency_word_count, '*.fb2'):
                op_file = open(file_frequency_word_count, encoding="utf8")
                data_to_read = op_file.read()
                words = data_to_read.split(" ")
                print(words)
                freqs = {}
                for w_cnts in words:
                    if w_cnts not in freqs:
                        freqs[w_cnts] = 1
                    else:
                        freqs[w_cnts] += 1
                        print(words,freqs[w_cnts])
    except Exception as error:
        logging.exception(error)

insertVariableIntoTable()
