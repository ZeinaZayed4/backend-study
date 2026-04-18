from database_connection import DatabaseConnection


def create_bookmarks_table(dbname="bookmarks_db"):
    db = DatabaseConnection(dbname=dbname)

    db.execute("DROP TABLE IF EXISTS bookmarks")

    db.execute("""
        CREATE TABLE bookmarks(
            id SERIAL PRIMARY KEY,
            url VARCHAR(500) UNIQUE NOT NULL,
            title VARCHAR(300),
            visits INTEGER DEFAULT 0,
            created_at TIMESTAMP DEFAULT NOW(),
            updated_at TIMESTAMP DEFAULT NOW()
        );
    """)

    db.close()


if __name__ == "__main__":
    create_bookmarks_table()
