import sqlite3

def create_database():
    conn = sqlite3.connect('quiz.db')
    conn.close()
  
# Function to create a table for storing name, email, and quiz score
def create_table():
    conn = sqlite3.connect('quiz.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS leaderboard
                 (id INTEGER PRIMARY KEY AUTOINCREMENT,
                 name TEXT,
                 email TEXT,
                 score INTEGER)''')
    conn.commit()
    conn.close()

# Function to add data into the database
def updatedb(name, email, score):
    conn = sqlite3.connect('quiz.db')
    c = conn.cursor()
    c.execute('''INSERT INTO leaderboard (name, email, score) VALUES (?, ?, ?)''', (name, email, score))
    conn.commit()
    conn.close()

def retrieve_leaderboard():
    conn = sqlite3.connect('quiz.db')
    c = conn.cursor()
    c.execute('''SELECT * FROM leaderboard ORDER BY score DSC''')  # Adding ORDER BY clause to sort by score in ascending order
    data = c.fetchall()
    conn.close()
    return data
