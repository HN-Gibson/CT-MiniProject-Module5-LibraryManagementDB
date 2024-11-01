from connect_mysql import connect_db
from mysql.connector import Error

def add_book():
    conn = connect_db()
    if conn is not None:    
        try:
            cursor = conn.cursor()    
            title = input("Enter the title:\n").lower()
            author = input("Enter the author's name:\n").lower()
            genre = input("Enter the genre:\n")
            pub_date = input("Enter the date of publication:\n(Enter in 'YYYY/MM/DD format')\n")

            new_book = (title,author,genre,pub_date)
        
            query = "INSERT INTO books(title,author_name,genre,publication_date) VALUES (%s,%s,%s,%s)"

            cursor.execute(query,new_book)
            conn.commit()
            print (f"{title.title()} has been added to the user database!")

        except Error as e:
            print(f"Error: {e}")

        finally:
            if conn and conn.is_connected():
                cursor.close()

def check_out_book():
    conn = connect_db()
    if conn is not None:    
        try: 
            cursor = conn.cursor()   
            book_id = input("Enter ID of book you would like to borrow:\n")
            user_id = input("Enter ID for user borrowing the book:\n")
        
            query = "SELECT availability FROM books WHERE id = %s"

            cursor.execute(query,(book_id,))
            result = cursor.fetchone()

            if result is None:
                print ("Book not found!")
                return
            
            available = result[0]

            if not available:
                print("This book is currently checked out.")
                return
            
            check_out_query = "INSERT INTO borrowed_books(user_id,book_id,borrow_date) VALUES (%s,%s,CURDATE())"
            
            cursor.execute(check_out_query,(user_id,book_id))

            availability_query = "UPDATE books SET availability = FALSE where id = %s"

            cursor.execute(availability_query,(book_id,))
           
            conn.commit()
            print("Book successfully checked out!")

        except Error as e:
            print(f"Error: {e}")

        finally:
            if conn and conn.is_connected():
                cursor.close()

def check_in_book():
    conn = connect_db()
    if conn is not None:
        try:
            cursor = conn.cursor()   
            book_id = input("Enter ID of book you would like to return:\n")
            user_id = input("Enter ID for user returning the book:\n")
        
            query = "SELECT availability FROM books WHERE id = %s"

            cursor.execute(query,(book_id,))
            result = cursor.fetchone()

            if result is None:
                print ("Book not found!")
                return
            
            available = result[0]

            if available:
                print("This book is currently available.")
                return
            
            check_out_query = "UPDATE borrowed_books SET return_date = CURDATE() WHERE user_id = %s AND book_id = %s"
            
            cursor.execute(check_out_query,(user_id,book_id))

            availability_query = "UPDATE books SET availability = true where id = %s"

            cursor.execute(availability_query,(book_id,))
           
            conn.commit()
            print("Book successfully checked in!")
            
        except Error as e:
            print(f"Error: {e}")

        finally:
            if conn and conn.is_connected():
                cursor.close()

def search_book():
    conn = connect_db()
    if conn is not None:
        try:
            cursor = conn.cursor()
            book_title = input("Enter title you would like to search:\n").lower()

            query = "SELECT * FROM books"

            cursor.execute(query)

            for row in cursor.fetchall():
                book_id,title,author,genre,pub_date,availability = row
                if book_title in title:
                    print(f"Book ID: {book_id}, Title: {title.title()}, Author: {author.title()}, Genre: {genre}, Date of Publication: {pub_date}, Available: {availability}")

        except Error as e:
            print(f"Error: {e}")

        finally:
            if conn and conn.is_connected():
                cursor.close()

def display_books():
    conn = connect_db()
    if conn is not None:    
        try:
            cursor = conn.cursor()

            query = "SELECT * FROM books"

            cursor.execute(query)

            for row in cursor.fetchall():
                book_id,title,author,genre,pub_date,availability = row
                print(f"Book ID: {book_id}, Title: {title.title()}, Author: {author.title()}, Genre: {genre}, Publication Year: {pub_date}, Available: {availability}")

        except Error as e:
            print(f"Error: {e}")

        finally:
            if conn and conn.is_connected():
                cursor.close()

def add_user():
    conn = connect_db()
    if conn is not None:
        try:
            cursor = conn.cursor()
            name = input("Enter the user's name:\n").lower()

            query = "INSERT INTO users(name) VALUES (%s)"

            cursor.execute(query,(name,))
            conn.commit()
            print (f"{name.title()} has been added to the user database!")

        except Error as e:
            print(f"Error: {e}")

        finally:
            if conn and conn.is_connected():
                cursor.close()

def view_user_detail():
    conn = connect_db()
    if conn is not None:
        try:
            cursor = conn.cursor()
            user = input("Enter ID of user you would like details for:\n")
            user_num = int(user)

            query = "SELECT * FROM users"

            cursor.execute(query)

            for row in cursor.fetchall():
                user_id,name = row
                if user_num == user_id:
                    print(f"User ID: {user_id}, Name: {name.title()}")

            borrowed_book_query = "SELECT * FROM borrowed_books WHERE user_id = %s"

            cursor.execute(borrowed_book_query,(user,))

            for row in cursor.fetchall():
                transaction_id,user_id,book_id,borrow_date,return_date = row
                if user_num == user_id:
                    print(f"Transaction ID: {transaction_id}, Book ID: {book_id}, Borrowed: {borrow_date}, Returned: {return_date}")

        except Error as e:
            print(f"Error: {e}")

        finally:
            if conn and conn.is_connected():
                cursor.close()

def display_users():
    conn = connect_db()
    if conn is not None:    
        try:
            cursor = conn.cursor()

            query = "SELECT * FROM users"
            
            cursor.execute(query)

            for row in cursor.fetchall():
                user_id,name = row
                print(f"User ID: {user_id}, Name: {name.title()}")

        except Error as e:
            print(f"Error: {e}")

        finally:
            if conn and conn.is_connected():
                cursor.close()

def add_author():
    conn = connect_db()
    if conn is not None:    
        try:
            cursor = conn.cursor()
            name = input("Enter the author's name:\n").lower()
            biography = input("Enter a brief bio about the author:\n")

            new_author = (name,biography)

            query = "INSERT INTO authors(name,biography) VALUES (%s, %s)"

            cursor.execute(query,new_author)
            conn.commit()
            print (f"{name.title()} has been added to the author database!")

        except Error as e:
            print(f"Error: {e}")

        finally:
            if conn and conn.is_connected():
                cursor.close()  

def view_author_detail():
    conn = connect_db()
    if conn is not None:    
        try:
            cursor = conn.cursor()
            author = input("Enter name for author you would like details for:\n").lower()

            query = "SELECT * FROM authors"

            cursor.execute(query)

            for row in cursor.fetchall():
                author_id,name,biography = row
                if author in name:
                    print(f"Author ID: {author_id}, Name: {name.title()}, Biography: {biography}")
        
        except Error as e:
            print(f"Error: {e}")

        finally:
            if conn and conn.is_connected():
                cursor.close()

def display_authors():
    conn = connect_db()
    if conn is not None:    
        try:
            cursor = conn.cursor()
            
            query = "SELECT * FROM authors"
            
            cursor.execute(query)

            for row in cursor.fetchall():
                author_id,name,biography = row
                print(f"Author ID: {author_id}, Name: {name.title()}, Biography: {biography}")

        except Error as e:
            print(f"Error: {e}")

        finally:
            if conn and conn.is_connected():
                cursor.close()           
    