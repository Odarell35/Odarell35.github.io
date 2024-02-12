import sqlite3

if __name__ == "__main__":
    conn = sqlite3.connect('instance/eBook_db.db')
    cur = conn.cursor()

    cur.execute("INSERT INTO books (title, Author, Catergory_name, Book_description, ref_link) VALUES(' Rise of the TMNT: Sound Off!',\
'Matthew K. Manning',\
'Animation',\
'In this ebook, the Teenage Mutant Ninja Turtles (TMNT) face new adversaries, challenging their cunning and skills. However, the key to victory lies in April finding her voice before it is too late. The story explores the turtles strategies and abilities as they confront these new threats.',\
'https://play.google.com/store/books/details/Matthew_K_Manning_TMNT_Rise_of_the_TMNT_Sound_Off?id=-GurDwAAQBAJ')")
conn.commit()
cur.close()
conn.close()

