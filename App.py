

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
    print( count_words)

print('book title')
for files_to_read_titles in nms:
    if fnmatch.fnmatch(files_to_read_titles, '*.fb2'):
        op_file = open(files_to_read_titles, encoding="utf8")
        data_to_read = op_file.read()
        start = '<book-title>'
        end = '</book-title>'
        print((data_to_read.split(start))[1].split(end)[0])

print('number_of_paragraph')
for files_to_read_titles in nms:
    if fnmatch.fnmatch(files_to_read_titles, '*.fb2'):
        op_file = open(files_to_read_titles, encoding="utf8")
        data_to_read = op_file.read()
        paragraphs = data_to_read.split("</p>")
        count_paragraphs = len(paragraphs)
        print(count_paragraphs)

print('number_of_letters')
for number_of_letters in nms:
    if fnmatch.fnmatch(number_of_letters, '*.fb2'):
        op_file = open(number_of_letters, encoding="utf8")
        data_to_read = op_file.read()
        count_letters = len(data_to_read)
        print(count_letters)


print('capital letters')
for words_in_file in nms:
    if fnmatch.fnmatch(words_in_file, '*.fb2'):
        op_file = open(words_in_file, encoding="utf8")
        data_to_read = op_file.read()
        #words = data_to_read.split(" ")
        #print(data_to_read)

#hash = {} #initialize an empty dictinonary
count1 = 0
count2 = 0
for word in words_in_file.split(" "):
    if word[0].islower():
        count1 = count1+1
    elif word[0].upper():
        count2 = count2+1
print(count1)
print(count2)

    #if word[0].isupper():
        #if word in hash:
            #hash[word] +=1
print('word')



print('insert into table')

conn = sqlite3.connect('Automation.db')
c = conn.cursor()

def data_entry():
    book_name = files_to_read_titles
    number_of_words = file_word_count
    c.execute("INSERT INTO for_all_files(book_name, number_of_paragraph, number_of_words, number_of_letters) VALUES (?,?,?,?)",
              (book_name, files_to_read_titles, number_of_words, number_of_letters))
    conn.commit()

def read_from_db():
    c.execute('SELECT * FROM for_all_files')
    #data = c.fetchall()
    #print(data)
    for row in c.fetchall():
        print(row)

c.close()
conn.close()


