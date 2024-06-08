class Book:
    def __init__(self, title: str, author: str, pages: int):
        self.title = title
        self.author = author
        self.pages = pages
    
    def __str__(self) -> str:
        return f"Title: {self.title}, Author: {self.author}, Pages: {self.pages}"
    
    

# Example:
book1 = Book("The Great Gatsby", "F. Scott Fitzgerald", 218)
print(book1)
