import sqlite3

def create_database():
    conn = sqlite3.connect('quiz.sqlite')
    conn.close()
  
# Function to create a table for storing name, email, and quiz score
def create_table():
    conn = sqlite3.connect('quiz.sqlite')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS leaderboard
                    (id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT,
                    email TEXT,
                    score INTEGER,
                    time INTEGER)''')
    conn.commit()
    conn.close()

# Function to add data into the database
def updatedb(name, email, score, time):
    conn = sqlite3.connect('quiz.sqlite')
    c = conn.cursor()
    c.execute('''INSERT INTO leaderboard (name, email, score, time) VALUES (?, ?, ?, ?)''', (name, email, score, time))
    conn.commit()
    conn.close()

def retrieve_leaderboard():
    conn = sqlite3.connect('quiz.sqlite')
    c = conn.cursor()
    c.execute('''SELECT * FROM leaderboard ORDER BY score DESC''')  # Adding ORDER BY clause to sort by score in ascending order
    data = c.fetchall()
    conn.close()

    
    sendthis = []
    for i in data:
        curnt = {}
        curnt["name"] = i[1]
        curnt["email"] = i[2]
        curnt["score"] = i[3]
        curnt["time"] = i[4]
        sendthis.append(curnt)

    return sendthis

if __name__ == '__main__':
    create_database()
    create_table()
