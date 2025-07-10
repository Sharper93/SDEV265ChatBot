import sqlite3

# Connect (this creates the file if it doesn't exist)
conn = sqlite3.connect('chatbot.db')
c = conn.cursor()

# Create the table
c.execute('''
CREATE TABLE IF NOT EXISTS qa_pairs (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    question TEXT NOT NULL,
    answer TEXT NOT NULL,
    timestamp TEXT DEFAULT CURRENT_TIMESTAMP
)
''')

conn.commit()
conn.close()

print("Database initialized with table 'qa_pairs'.")