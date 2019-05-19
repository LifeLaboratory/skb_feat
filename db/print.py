import sqlite3

conn = sqlite3.connect('general.db')
c = conn.cursor()
data = c.execute("SELECT * FROM events").fetchall()
print(data)
c.close()
conn.close()