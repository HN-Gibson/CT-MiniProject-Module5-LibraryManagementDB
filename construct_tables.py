from connect_mysql import connect_db


conn = connect_db()
if conn is not None:
    try:
        cursor=conn.cursor()
        query =   """
            CREATE TABLE books (
            id INT AUTO_INCREMENT PRIMARY KEY,
            title VARCHAR(255) NOT NULL,
            author_name VARCHAR(255) NOT NULL,
            genre VARCHAR(255) NOT NULL,
            publication_date DATE,
            availability BOOLEAN DEFAULT 1
            );

            CREATE TABLE authors (
            id INT AUTO_INCREMENT PRIMARY KEY,
            name VARCHAR(255) NOT NULL,
            biography TEXT
            );

            CREATE TABLE users (
            id INT AUTO_INCREMENT PRIMARY KEY,
            name VARCHAR(255) NOT NULL
            );

            CREATE TABLE borrowed_books (
            id INT AUTO_INCREMENT PRIMARY KEY,
            user_id INT,
            book_id INT,
            borrow_date DATE NOT NULL,
            return_date DATE,
            FOREIGN KEY (user_id) REFERENCES users(id),
            FOREIGN KEY (book_id) REFERENCES books(id)
            );
            """
        cursor.execute(query)
    finally:
        if conn and conn.is_connected():
            cursor.close()
            conn.close()
            print("MySQL connection is closed.")