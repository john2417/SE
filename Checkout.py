class Checkout:
    def __init__(self, id, name, isbn, title):
        self.id = id
        self.name = name
        self.isbn = isbn
        self.title = title
        
    
    def write(self,fs):
        fs.write(self.id+",")
        fs.write(self.name+",")
        fs.write(self.isbn+",")
        fs.write(self.title+"\n")
        
        
    @staticmethod
    def load_checkout(fs):
        data = fs.readline()
        elems = data.split(",")
        if len(elems)<4:
            return None
        id = elems[0]
        name = elems[1]
        isbn = elems[2]
        title = elems[3]
        
        return Checkout(id, name, isbn,title)