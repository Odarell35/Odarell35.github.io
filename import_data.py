import sqlite3

if __name__ == "__main__":
    conn = sqlite3.connect('instance/eBook_db.db')
    cur = conn.cursor()

    cur.execute("INSERT INTO books (title, Author, Catergory_name, Book_description, ref_link) VALUES('The  Bee  sting','Paul  Murray','Fiction','The  Barnes  family  faces  a  crisis  as  Dickie`s  profitable  car  business  collapses,  yet  he`s  preoccupied  building  an  apocalypse-proof  bunker  with  a  rebellious  handyman.  Imelda,  his  wife,  resorts  to  selling  jewelry  online  and  navigating  advances  from  cattle  farmer  Big  Mike.  Meanwhile,  their  once  high-achieving  daughter  Cass  is  prioritizing  binge  drinking  over  exams.  Twelve-year-old  PJ  contemplates  running  away,  highlighting  the  family`s  unraveling  dynamics  amid  financial  woes  and  personal  struggles.', 'https://play.google.com/store/books/details/Paul_Murray_The_Bee_Sting?id=QJmDEAAAQBAJ')")
    conn.commit()
    cur.close()
    conn.close()

