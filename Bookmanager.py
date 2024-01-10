from Book import book
from Db import db

class bookmanager(object):
    def __init__(self):
        self.dbManager = db('book.data')    
        self.booklist = self.dbManager.read()

    def append(self, book):
        self.booklist.append(book)

    def showbooks(self):
        for book in self.booklist:
            book.greeting()
    
    def removebook(self, title):
        target = None
        for book in self.booklist:
            if book.title == title:
                target = book

        if target != None:
            self.booklist.remove(target)
    
    def modifybook(self, title, title2):
        target = None
        for book in self.booklist:
            if book.title == title:
                target = book
        if target == None:
            print('no book')
        if target != None:
            target.setTitle(title2)

    def save(Self):
        self.dbManager.save(self.booklist)
