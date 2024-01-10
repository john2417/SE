class book (object):
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def greeting(self):
        print("Book name : " + self.title)
        print("Autor : " + self.author)

    def setTitle(self, title):
        self.title = title

    def toString(self):
        return self.title + "," + self.author + '/n'