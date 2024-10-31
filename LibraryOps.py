from connect_mysql import connect_db
from mysql.connector import Error

def add_book():
    conn = connect_db()
    if conn is not None:    
        try:
            cursor = conn.cursor()    
            title = input("Enter the title:\n")
            author = input("Enter the author:\n")
            genre = input("Enter the genre:\n")
            pub_date = input("Enter the date of publication:\n")
        
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
            title = input("Enter title of book you would like to borrow:\n")
            user_id = input("Enter User ID for person borrowing the book:\n")
        
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
            title = input("Enter title of book you would like to return:\n")
            user_id = input("Enter User ID for person returning the book:\n")
        
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
            title = input("Enter title you would like to search:\n")
        
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
            name = input("Enter the user's name:\n")
            user_id = input("Create a unique User ID:\n")
        
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
            user_id = input("Enter User ID for user you would like details for:\n")
        
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
            name = input("Enter the author's name:\n")
            biography = input("Enter a brief bio about the author:\n")

            new_author = (name,biography)

            query = "INSERT INTO authors(name,biography) VALUES (%s, %s)"

            cursor.execute(query,new_author)
            conn.commit()
            print (f"{name} has been added to the database!")

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
            author = input("Enter name for author you would like details for:\n")
        
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
                print(f"Author ID: {author_id}, Name: {name}, Biography: {biography}")

        except Error as e:
            print(f"Error: {e}")

        finally:
            if conn and conn.is_connected():
                cursor.close()           
    