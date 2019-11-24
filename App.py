

import os
import shutil
import fnmatch
import glob #, re, errno, sys
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
#book_name = re.match("(<book-title>\w+)\W(</book-title>\w+)",data_contents)
#book_name = re.findall("<book-title>\w+",data_contents)
#book_name_end = re.findall(r"<\book\-\title\>(.*)\<\book\-\title\>",data_contents)
#book_name = re.search(r"<book-title>\(([^)(]*)\)</book-title>",data_contents)
#print('Book name ' ,book_name)
#print('Book name ' ,book_name_end)

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
print('C:\Automation\Input', file_names)
pth = 'C:\Automation\Input\*.fb2'
nms = glob.glob(pth)
print(nms)
for files_to_read in nms:
    #if files_to_read.endswith('.fb2'):
    if fnmatch.fnmatch(files_to_read, '*.fb2'):
        op_file = open(files_to_read, encoding="utf8")
        data_to_read = op_file.read()
        print(data_to_read)
print(files_to_read)


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
print(files)
for file in os.listdir('C:\Automation\Input'):
    with open(file,"r") as f:
        for line in f.readlines():
            print(line.split())
