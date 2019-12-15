import sqlite3
from App import files_to_read_titles
from App import number_of_paragraph_real
from App import file_word_count_real
from App import number_of_letters_real
from App import words_with_capital_letters_real
from App import words_in_lower_case_real

conn = sqlite3.connect('Automation.db')
c = conn.cursor()

# def create_table():
#     c.execute('CREATE TABLE IF NOT EXISTS for_all_files '
#               '( '
#               'book_name TEXT'
#               ', number_of_paragraph INTEGER'
#               ', number_of_words INTEGER'
#               ', number_of_letters INTEGER'
#               ', words_with_capital_letters INTEGER'
#               ', words_in_lower_case INTEGER'
#               ')')
#
# def data_entry():
#     c.execute("INSERT INTO for_all_files VALUES ('good', 56, 766, 65, 788, 5678)")
#     conn.commit()
#     c.close()
#     conn.close()
#
# create_table()
# data_entry()

# def data_entry():
    # book_name = files_to_read_titles
    # number_of_paragraph = number_of_paragraph_real
    # number_of_words = file_word_count_real
    # number_of_letters = number_of_letters_real
    # words_with_capital_letters = words_with_capital_letters_real
    # words_in_lower_case = words_in_lower_case_real
values_to_insert = [files_to_read_titles, number_of_paragraph_real, file_word_count_real, number_of_letters_real, words_with_capital_letters_real, words_in_lower_case_real]
#print(values_to_insert)
c.executemany("INSERT INTO for_all_files"
              "("
              "book_name"
              ", number_of_paragraph"
              ", number_of_words"
              ", number_of_letters"
              ", words_with_capital_letters"
              ", words_in_lower_case"
              ") VALUES (?,?,?,?,?,?)", [values_to_insert]
              #(book_name, number_of_paragraph, number_of_words, number_of_letters, words_with_capital_letters, words_in_lower_case)
                  )
conn.commit()

# def read_from_db():
#     c.execute('SELECT * FROM for_all_files')
#     #data = c.fetchall()
#     #print(data)
#     for row in c.fetchall():
#         print(row)

c.close()
conn.close()

