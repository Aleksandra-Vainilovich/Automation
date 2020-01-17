

import os
import shutil
import fnmatch
import glob
import sqlite3
#, re, errno, sys
#os.chdir('c:\Automation\Input')



print('move files with incorrect ')
files = os.listdir('C:\\Automation\\Input')
print(files)
for new_file in files:
    if not fnmatch.fnmatch(new_file, '*.fb2'):
        shutil.move(new_file,'C:\Automation\Incorrect_input')

print('open and read file')
path = 'C:\Automation\Input\Example.fb2'
file_name = ('Example.fb2')
data = open(path, encoding="utf8")
data_contents = data.read()
#print(data_contents)

print('words count')
words = data_contents.split(" ")
count_words = len(words)
print('Number of words ', count_words)

print('book title')
start = '<book-title>'
end = '</book-title>'
print((data_contents.split(start))[1].split(end)[0])
print((data_contents.split(start))[2].split(end)[0])

print('read all files in folder')
file_names = os.listdir('C:\Automation\Input')
print(file_names)
pth = 'C:\Automation\Input\*.fb2'
nms = glob.glob(pth)
print(nms)
for files_to_read in nms:
    if fnmatch.fnmatch(files_to_read, '*.fb2'):
        op_file = open(files_to_read, encoding="utf8")
        data_to_read = op_file.read()
        #print(data_to_read)

print('all files words count')
for file_word_count in nms:
    op_file = open(file_word_count, encoding="utf8")
    data_to_read = op_file.read()
    words = data_to_read.split(" ")
    count_words = len(words)
    start = '<book-title>'
    end = '</book-title>'
    print((data_to_read.split(start))[1].split(end)[0], ': count of words', count_words)

# for file_word_count_real in nms:
#     op_file = open(file_word_count_real, encoding="utf8")
#     data_to_read = op_file.read()
#     words = data_to_read.split(" ")
#     count_words = len(words)
#     print(count_words)

def file_word_count_int():
    for file_word_count_real in nms:
        op_file = open(file_word_count_real, encoding="utf8")
        data_to_read = op_file.read()
        words = data_to_read.split(" ")
        count_words = len(words)
        print(count_words)

file_word_count_int()

print('book title')
# for files_to_read_titles in nms:
#     if fnmatch.fnmatch(files_to_read_titles, '*.fb2'):
#         op_file = open(files_to_read_titles, encoding="utf8")
#         data_to_read = op_file.read()
#         start = '<book-title>'
#         end = '</book-title>'
#         print((data_to_read.split(start))[1].split(end)[0])

def files_to_read_titles_text():
    for files_to_read_titles in nms:
        if fnmatch.fnmatch(files_to_read_titles, '*.fb2'):
            op_file = open(files_to_read_titles, encoding="utf8")
            data_to_read = op_file.read()
            start = '<book-title>'
            end = '</book-title>'
            print((data_to_read.split(start))[1].split(end)[0])

files_to_read_titles_text()

print('number_of_paragraph')
for number_of_paragraph in nms:
    if fnmatch.fnmatch(number_of_paragraph, '*.fb2'):
        op_file = open(number_of_paragraph, encoding="utf8")
        data_to_read = op_file.read()
        paragraphs = data_to_read.split("</p>")
        count_paragraphs = len(paragraphs)
        start = '<book-title>'
        end = '</book-title>'
        print((data_to_read.split(start))[1].split(end)[0], ': count of paragraphs',count_paragraphs)

# for number_of_paragraph_real in nms:
#     if fnmatch.fnmatch(number_of_paragraph_real, '*.fb2'):
#         op_file = open(number_of_paragraph_real, encoding="utf8")
#         data_to_read = op_file.read()
#         paragraphs = data_to_read.split("</p>")
#         count_paragraphs = len(paragraphs)
#         print(count_paragraphs)

def number_of_paragraph_int():
    for number_of_paragraph_real in nms:
        if fnmatch.fnmatch(number_of_paragraph_real, '*.fb2'):
            op_file = open(number_of_paragraph_real, encoding="utf8")
            data_to_read = op_file.read()
            paragraphs = data_to_read.split("</p>")
            count_paragraphs = len(paragraphs)
            print(count_paragraphs)

number_of_paragraph_int()

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

def number_of_letters_int():
    for number_of_letters_real in nms:
        if fnmatch.fnmatch(number_of_letters_real, '*.fb2'):
            op_file = open(number_of_letters_real, encoding="utf8")
            data_to_read = op_file.read()
            count_letters = len(data_to_read)
            print(count_letters)

number_of_letters_int()

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

# for words_with_capital_letters_real in nms:
#     if fnmatch.fnmatch(words_with_capital_letters_real, '*.fb2'):
#         op_file = open(words_with_capital_letters_real, encoding="utf8")
#         data_to_read = op_file.read()
#         words = data_to_read.split(" ")
#         print(sum(1 for cnt_upper in words if cnt_upper.isupper()))

def words_with_capital_letters_int():
    for words_with_capital_letters_real in nms:
        if fnmatch.fnmatch(words_with_capital_letters_real, '*.fb2'):
            op_file = open(words_with_capital_letters_real, encoding="utf8")
            data_to_read = op_file.read()
            words = data_to_read.split(" ")
            print(sum(1 for cnt_upper in words if cnt_upper.isupper()))

words_with_capital_letters_int()

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

# for words_in_lower_case_real in nms:
#     if fnmatch.fnmatch(words_in_lower_case_real, '*.fb2'):
#         op_file = open(words_in_lower_case_real, encoding="utf8")
#         data_to_read = op_file.read()
#         words = data_to_read.split(" ")
#         print(sum(1 for cnt_lower in words if cnt_lower.islower()))
# print(words_in_lower_case_real)

def words_in_lower_case_int():
    for words_in_lower_case_real in nms:
        if fnmatch.fnmatch(words_in_lower_case_real, '*.fb2'):
            op_file = open(words_in_lower_case_real, encoding="utf8")
            data_to_read = op_file.read()
            words = data_to_read.split(" ")
            print(sum(1 for cnt_lower in words if cnt_lower.islower()),'gjhj')

words_in_lower_case_int()

#print(words_in_lower_case_int(), words_with_capital_letters_int(), 'hghhghhghghgh', sep=',')

print('All values in one row')
def values_list():
    for values in nms:
        if fnmatch.fnmatch(values, '*.fb2'):
            op_file = open(values, encoding="utf8")
            data_to_read = op_file.read()
            #book_name
            start = '<book-title>'
            end = '</book-title>'
            #number_of_paragraph
            paragraphs = data_to_read.split("</p>")
            count_paragraphs = len(paragraphs)
            #number_of_words
            words = data_to_read.split(" ")
            count_words = len(words)
            #number_of_letters
            count_letters = len(data_to_read)
            #words_with_capital_letters
            #words_in_lowercase
            a=("'"+(data_to_read.split(start))[1].split(end)[0]+"'"
                  ,int(count_paragraphs)
                  ,int(count_words)
                  ,int(count_letters)
                  ,int(sum(1 for cnt_upper in words if cnt_upper.isupper()))
                  ,int(sum(1 for cnt_lower in words if cnt_lower.islower()))
                  )
            print(a,',')

values_list()
print('ttttttttttttttttt')
data_g = str(values_list())
#print(data_g, sep=',')
print('yyyyyyyyyyyyy')
g = data_g.split('\n')
print(g)
# print('hhhhhhhhhhhhh')
# print(data_g)
# print('fffffffffffff')
# print(values_list())
# for string in data_g or []:
#     a = string.split(',')
#     print(a)

print('insert into table')

# conn = sqlite3.connect('Automation.db')
# c = conn.cursor() #Cursor creation
# #
# #def data_entry():
# #     book_name = files_to_read_titles
# #     number_of_paragraph = number_of_paragraph_real
# #     number_of_words = file_word_count_real
# #     number_of_letters = number_of_letters_real
# #     words_with_capital_letters = words_with_capital_letters_real
# #     words_in_lower_case = words_in_lower_case_real
# #values_to_insert = [(files_to_read_titles_text(),), (number_of_paragraph_int(),), (file_word_count_int(),), (number_of_letters_int(),), (words_with_capital_letters_int(),), (words_in_lower_case_int(),),]
# #values_to_insert = [files_to_read_titles_text(), number_of_paragraph_int(), file_word_count_int(), number_of_letters_int(), words_with_capital_letters_int(), words_in_lower_case_int()]
# #values_to_insert = [[files_to_read_titles_text()], [number_of_paragraph_int()], [file_word_count_int()], [number_of_letters_int()], [words_with_capital_letters_int()], [words_in_lower_case_int()]]
# #values_to_insert = [print([files_to_read_titles_text()]), print([number_of_paragraph_int()]), print([file_word_count_int()]), print([number_of_letters_int()]), print([words_with_capital_letters_int()]), print([words_in_lower_case_int()])]
#
# #values_to_insert = [print([values_list()])]
# #values_to_insert = print([values_list()])
# values_to_insert = values_list()
#
# def table_insert():
#    c.execute("INSERT INTO for_all_files (book_name, number_of_paragraph, number_of_words, number_of_letters, words_with_capital_letters, words_in_lower_case) VALUES (?,?,?,?,?,?)", [values_to_insert])
#
#
# # def table_insert():
# #     c.execute("""INSERT INTO for_all_files VALUES
# #                                     (
# #                                     files_to_read_titles_text()
# #                                     , number_of_paragraph_int()
# #                                     , file_word_count_int()
# #                                     , number_of_letters_int()
# #                                     , words_with_capital_letters_int()
# #                                     , words_in_lower_case_int()
# #                                     )"""
# #               )
# table_insert()
#
# conn.commit()
#
# # def read_from_db():
# #     c.execute('SELECT * FROM for_all_files')
# #     #data = c.fetchall()
# #     #print(data)
# #     for row in c.fetchall():
# #         print(row)
#
# c.close()
# conn.close() #Closing connection with the database
# #print(values_to_insert)
#
#
#
#
