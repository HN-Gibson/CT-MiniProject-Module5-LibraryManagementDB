from BookOps import Book
from UserOps import User
from AuthorOps import Author
from ErrorHandling import BookNotFound
from ErrorHandling import UserNotFound
from ErrorHandling import AuthorNotFound

class Library:
    def __init__(self):
        self.library = {}
        self.user_database = {}
        self.author_database = {}

    def check_out_book(self):
        try:    
            title = input("Enter title of book you would like to borrow:\n")
            user_id = input("Enter User ID for person borrowing the book:\n")
            book_to_borrow = self.library.get(title)
            borrower = self.user_database.get(user_id)
            if book_to_borrow == None:
                raise BookNotFound
            elif borrower == None:
                raise UserNotFound
            else:
                Book.borrow_book(book_to_borrow)
                User.add_borrowed_books(borrower,title)
            print (f"{title} has been borrowed by {user_id}!")    
        except BookNotFound:
            BookNotFound.handle_book_not_found()
        except UserNotFound:
            UserNotFound.handle_user_not_found()            

    def check_in_book(self):
        try:    
            title = input("Enter title of book you would like to return:\n")
            user_id = input("Enter User ID for person returning the book:\n")
            book_to_return = self.library.get(title)
            borrower = self.user_database.get(user_id)
            if book_to_return == None:
                raise BookNotFound
            elif borrower == None:
                raise UserNotFound            
            else:
                Book.return_book(book_to_return)
                User.remove_borrowed_books(borrower,title)
                print (f"{title} has been returned by {user_id}!")
        except BookNotFound:
            BookNotFound.handle_book_not_found()
        except UserNotFound:
            UserNotFound.handle_user_not_found()    
    
    def add_book(self):
        title = input("Enter the title:\n")
        author = input("Enter the author:\n")
        genre = input("Enter the genre:\n")
        pub_date = input("Enter the date of publication:\n")
        self.library[title] = Book(title,author,genre,pub_date)
        print (f"'{title}' Added!")
    
    def search_book(self):
        try:
            title = input("Enter title you would like to search:\n")
            book_data = self.library.get(title)
            if book_data == None:
                raise BookNotFound
            else:
                print(book_data)
        except BookNotFound:
            BookNotFound.handle_book_not_found()
    
    def display_books(self):
        if self.library == {}:
            print("No books in library!")
        else:
            for title in self.library:
                print(f"'{title}'")
    
    def add_user(self):
        name = input("Enter the user's name:\n")
        user_id = input("Create a unique User ID:\n")
        self.user_database[user_id] = User(name,user_id)
        print (f"{name} created a profile with {user_id} as their User ID!")

    def view_user_detail(self):
        try:
            user_id = input("Enter User ID for user you would like details for:\n")
            user_data = self.user_database.get(user_id)
            if user_data == None:
                raise UserNotFound
            else:
                print(user_data)
        except UserNotFound:
            UserNotFound.handle_user_not_found()

    def display_users(self):
        if self.user_database == {}:
            print("No users in database!")
        else:
            for user_id in self.user_database:
                print(f"User ID: {user_id}")
    
    def add_author(self):
        name = input("Enter the author's name:\n")
        biography = input("Enter a brief bio about the autho:\n")
        self.author_database[name] = Author(name,biography)
        print (f"Added {name} to the system!")
    
    def view_author_detail(self):
        try:
            author = input("Enter name for author you would like details for:\n")
            author_data = self.author_database.get(author)
            if author_data == None:
                raise AuthorNotFound
            else:
                print(author_data)
        except AuthorNotFound:
            AuthorNotFound.handle_author_not_found()
    
    def display_authors(self):
        if self.author_database == {}:
            print("No users in database!")
        else:
            for name in self.author_database:
                print(f"{name}")

    