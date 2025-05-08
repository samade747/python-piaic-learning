# Class Methods
# Create a class Book with a class variable total_books. Add a class method 
# increment_book_count() to increase the count when a new book is added.


class Book():
    #Class variabe bnaiya jo sab books ke liye common hai
    total_books = 0

    def __init__(self, title):
        self.title = title
        Book.increment_book_count()


    @classmethod
    def increment_book_count(cls):
        cls.total_books += 1 # Class variable ko 1 add hoga



book1 = Book("py learning")
book2 = Book("ai learning")


# out put
print(book1.total_books)
print(book2.total_books)

print("total books", Book.total_books) # class se bhi access kiya ja sakta hai