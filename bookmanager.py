class bookmanager (object):
    def __init__(self):
        self.booklist = []

    def appendbook(self, book):
        self.booklist.append(book)

    def showbooks(self):
        for book in self.booklist:
            book.greeting()