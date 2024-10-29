class Book:
    def __init__(self,title,author,genre,pub_date):
        self.__title = title
        self.__author = author
        self.__genre = genre
        self.__pub_date = pub_date
        self.__available = "Available"
 
    # def get_title(self):
    #     return self.__title
    # def get_author(self):
    #     return self.__author   
    # def get_genre(self):
    #     return self.__genre   
    # def get_pub_date(self):
    #     return self.__pub_date
    # def get_available(self):
    #     return self.__available
    def borrow_book(self):
        if self.__available == "Available":
            self.__available = "Borrowed"
    def return_book(self):
        self.__available = "Available" 
    def __repr__(self):
        return f"\nTitle: '{self.__title}'\nAuthor: {self.__author}\nGenre: {self.__genre}\nYear of Publication: {self.__pub_date}\n{self.__available}\n"




