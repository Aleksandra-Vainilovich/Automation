import sqlite3

conn = sqlite3.connect('Automation.db')
c = conn.cursor()

def create_table():
    c.execute('CREATE TABLE IF NOT EXISTS for_all_files ( book_name TEXT, number_of_paragraph REAL, number_of_words REAL, number_of_letters REAL, words_with_capital_letters REAL)')

def data_entry():
    c.execute("INSERT INTO for_all_files VALUES ('good', 56, 766, 65, 788)")
    conn.commit()
    c.close()
    conn.close()

create_table()
data_entry()