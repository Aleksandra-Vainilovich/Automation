

import os, shutil, fnmatch, re, glob, errno, sys
#source = 'C:\Automation\Input'
#destination = 'C:\Automation\Incorrect_input'
files = os.listdir('C:\Automation\Input')
print(files)
for new_file in files:
    if not fnmatch.fnmatch(new_file, '*.fb2'):
        shutil.move(new_file,'C:\Automation\Incorrect_input')


#df = pandas.read(r'C:\Automation\Input\Example.fb2')
#words_count = df.count().sum()
path = 'C:\Automation\Input\Example.fb2'
file_name = ('Example.fb2')
#data = open(file_name, encoding="utf8")
data = open(path, encoding="utf8")
data_contents = data.read()
#print(data_contents)
#book_name = re.match("(<book-title>\w+)\W(</book-title>\w+)",data_contents)
#book_name = re.findall("<book-title>\w+",data_contents)
#book_name_end = re.findall(r"<\book\-\title\>(.*)\<\book\-\title\>",data_contents)
#book_name = re.search(r"<book-title>\(([^)(]*)\)</book-title>",data_contents)
#print('Book name ' ,book_name)
#print('Book name ' ,book_name_end)

#def count_of_words(data_contents):
words = data_contents.split(" ")
count_words = len(words)
#return count_words

print('Number of words ', count_words)

start = '<book-title>'
end = '</book-title>'
print((data_contents.split(start))[1].split(end)[0])
print((data_contents.split(start))[2].split(end)[0])


#files = []
for file in os.listdir('C:\Automation\Input'):
    if file.endswith('.fb2'):
        with open(file, encoding="utf8") as op_file:
            data=op_file.read()
#print(data)
words = data_contents.split(" ")
count_words = len(words)
print('Number of words ', count_words)
#with open('Example.fb2','r', encoding="utf8") as f:
    #file_body = f.read()
    #wordcount = len(file_body,split())
#print(wordcount)

#path = 'C:\Automation\Input\*.fb2'
#files = glob.glob(path)
#print(files)
#for name in files

path = 'C:/Automation/Input/*.fb2'
files = os.listdir('C:\Automation\Input')
print (files)
for file in os.listdir('C:\Automation\Input'):
    with open(file,"r") as f:
        for line in f.readlines():
            print(line.split())
