class Database:
    def __init__(self,filename):
        self.filename = filename
        self.users=None
        self.file=None
        self.load()

    def load(self):
        self.file = open(self.filename,"r")
        self.users = { }

        for line in self.file:
            email,password,name,created = line.strip().split(";")
            self.users[email] = (password,name,created)

        self.file.close()
        pass

    def get_user(self,email):
        if email in self.users:
            return self.users[email]
        else:
            return -1

    def addd_user(self,email,password,name):
        if email.strip() not in self.users:
