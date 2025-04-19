import sqlite3

def init_db():
    conn = sqlite3.connect("snake_game.db")
    cursor = conn.cursor()

    # Create user table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS user (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE,
            level INTEGER DEFAULT 1
        )
    ''')

    # Create user_score table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS user_score (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER,
            score INTEGER,
            state TEXT,
            date TEXT DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY(user_id) REFERENCES user(id)
        )
    ''')

    conn.commit()
    conn.close()
    print("Database initialized.")

if __name__ == "__main__":
    init_db()
