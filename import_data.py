import sqlite3

if __name__ == "__main__":
    conn = sqlite3.connect('instance/eBook_db.db')
    cur = conn.cursor()
    

    cur.execute("INSERT INTO category (category_name) VALUES ('Romance'), ('History')")
    conn.commit()
    cur.close()
    conn.close()

