from ErrorHandling import UserInputEmpty
from ErrorHandling import InvalidEntry
from LibraryOps import Library


class UserInterface:
    def __init__(self):
        self.library = Library()
    def main(self):
        while True:
            try:
                print("""
                      Welcome to the Library Management System!

                        Main Menu:
                        1. Book Operations
                        2. User Operations
                        3. Author Operations
                        4. Quit
                      """)
                user_request = input("Please enter the number associated with the operations you would like to access:\n")
                if user_request == "":
                    raise UserInputEmpty
                elif user_request == "1":
                    self.book_operations()
                elif user_request == "2":
                    self.user_operations()
                elif user_request == "3":
                    self.author_operations()
                elif user_request == "4":
                    break
                else:
                    raise InvalidEntry
            except UserInputEmpty:
                UserInputEmpty.handle_user_input_empty()
            except InvalidEntry:
                InvalidEntry.handle_invalid_entry()
        print("Thank you for using my program!")

    def book_operations(self):
        while True:
            try:
                print("""
                    Book Operations:
                        1. Add a new book
                        2. Borrow a book
                        3. Return a book
                        4. Search for a book
                        5. Display all books
                        6. Return to Main Menu
                      """)
                user_request = input("Please enter the number associated with the operation you would like to perform:\n")
                if user_request == "":
                    raise UserInputEmpty
                elif user_request == "1":
                    self.library.add_book()     
                elif user_request == "2":
                    self.library.check_out_book()
                elif user_request == "3":
                    self.library.check_in_book()
                elif user_request == "4":
                    self.library.search_book()
                elif user_request == "5":
                    self.library.display_books()
                elif user_request == "6":
                    break
                else:
                    raise InvalidEntry
            except UserInputEmpty:
                UserInputEmpty.handle_user_input_empty()
            except InvalidEntry:
                InvalidEntry.handle_invalid_entry()

    def user_operations(self):
        while True:
            try:
                print("""
                    User Operations:
                        1. Add a new user
                        2. View user details
                        3. Display all users
                        4. Return to Main Menu
                      """)
                user_request = input("Please enter the number associated with the operation you would like to perform:\n")
                if user_request == "":
                    raise UserInputEmpty
                elif user_request == "1":
                    self.library.add_user()
                elif user_request == "2":
                    self.library.view_user_detail()
                elif user_request == "3":
                    self.library.display_users()
                elif user_request == "4":
                    break
                else:
                    raise InvalidEntry
            except UserInputEmpty:
                UserInputEmpty.handle_user_input_empty()
            except InvalidEntry:
                InvalidEntry.handle_invalid_entry()

    def author_operations(self):
        while True:
            try:
                print("""
                    Author Operations:
                        1. Add a new author
                        2. View author details
                        3. Display all authors
                        4. Return to Main Menu
                      """)
                user_request = input("Please enter the number associated with the operation you would like to perform:\n")
                if user_request == "":
                    raise UserInputEmpty
                elif user_request == "1":
                    self.library.add_author()
                elif user_request == "2":
                    self.library.view_author_detail()
                elif user_request == "3":
                    self.library.display_authors()
                elif user_request == "4":
                    break
                else:
                    raise InvalidEntry
            except UserInputEmpty:
                UserInputEmpty.handle_user_input_empty()
            except InvalidEntry:
                InvalidEntry.handle_invalid_entry()