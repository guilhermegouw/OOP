class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    def description(self):
        return f"Title: {self.title}, Author: {self.author}, Pages: {self.pages}"
