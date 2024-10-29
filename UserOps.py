class User:
    def __init__(self,name,id):
        self.__name = name
        self.__user_id = id
        self.__borrowed_books = []
    
    # def get_name(self):
    #     return self.__name
    # def get_id(self):
    #     return self.__user_id
    # def get_borrowed_books(self):
    #     return self.__borrowed_books
    def add_borrowed_books(self,title):
        self.__borrowed_books.append(title)
    def remove_borrowed_books(self,title):
        self.__borrowed_books.remove(title)
    def __repr__(self):
        return f"\nUser ID: '{self.__user_id}'\nName: {self.__name}\nBorrowed Books: {self.__borrowed_books}\n"
