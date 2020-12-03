import sqlite3
conn = sqlite3.connect('new_user.db')
c = conn.cursor()
# c.execute("drop table users")
c.execute("""CREATE TABLE IF NOT EXISTS users (
                id text,
                level text)""")
# c.execute("INSERT INTO users VALUES('vuai', 'moderate')")
# c.execute("DELETE FROM users")


c.execute("SELECT * FROM users")
c.fetchone()
conn.commit()
conn.close()


