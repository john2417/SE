class User:
    def __init__(self,id,name,birth_d,phone_n,email,ban = True):
        self.id = id
        self.name = name
        self.birth_d = birth_d
        self.phone_n = phone_n
        self.email = email
        self.ban = ban
        
    def write(self,fs):
        fs.write(str(self.id)+",")
        fs.write(self.name+",")
        fs.write(str(self.birth_d)+",")
        fs.write(str(self.phone_n)+",")
        fs.write(self.email+",")
        fs.write(str(self.ban)+"\n")
    @staticmethod
    def load_user(fs):
        data = fs.readline()
        elems = data.split(",")
        if len(elems)<5:
            return None
        id = int(elems[0])
        name = elems[1]
        birth_d = int(elems[2])
        phone_n = elems[3]
        email = elems[4]
        ban = elems[5]
        
        return User(id,name,birth_d ,phone_n,email,ban)
    
    