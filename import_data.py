import sqlite3

if __name__ == "__main__":
    conn = sqlite3.connect('instance/eBook_db.db')
    cur = conn.cursor()

    cur.execute("INSERT INTO books (title, Author, Catergory_name, Book_description, ref_link) VALUES('One Wrong Move (Jeopardy Falls Book #1)','Dani Pettrey', 'Romance', '""Taunting riddles. A deadly string of heists. Two broken hearts trapped in a killers game."" Christian O`Brady, once ensnared in a life of crime by his con artist parents, now strives to make amends as a leading security expert. However, when a series of Southwestern art heists target a gallery he secured, Christian finds himself teamed up with Andi Forester, a gifted insurance investigator with her own complicated past.Andi, a former brilliant FBI forensic analyst, saw her career crumble due to false accusations. Now, she channels her skills into investigating insurance fraud. The duo faces a high-stakes case, drawing them into a perilous game orchestrated by an adversary seeking revenge. As they race against time to catch the perpetrator, the danger intensifies, and one wrong move could prove fatal for them both. This gripping narrative unfolds as a thrilling tale of redemption, betrayal, and the intertwining fates of two individuals navigating a treacherous path set by a cunning adversary. The stakes are high, the tension palpable, and the clock is ticking in this deadly game of cat and mouse.', 'https://play.google.com/store/books/details/Dani_Pettrey_One_Wrong_Move_Jeopardy_Falls_Book_1?id=lcrIEAAAQBAJ')")
conn.commit()
cur.close()
conn.close()

