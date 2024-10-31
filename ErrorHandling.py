
class UserInputEmpty(Exception):
    pass
    def handle_user_input_empty():
        print("User Input Empty. Please try again.")          
class InvalidEntry(Exception):
    pass
    def handle_invalid_entry():
        print("Invalid Entry. Please try again.")
class BookNotFound(Exception):
    pass
    def handle_book_not_found():
        print("No book found by that name.")
class UserNotFound(Exception):
    pass
    def handle_user_not_found():
        print("No user found with that User ID.")
class AuthorNotFound(Exception):
    pass
    def handle_author_not_found():
        print("No author found with that name.")
class MissingRequiredData(Exception):
    pass
    def handle_missing_required_data():
        print ("Error: Missing required data.")