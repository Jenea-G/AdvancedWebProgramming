# create a class User
# give two attributes (username, password)
    # if password is less than 4 characters long, return an error! (can be just a print statement)

class User:
    def __init__ (self, un, pw):
        # option A:
        if len(pw) < 4:
            print("invalid password, it must beat least 4 characters long")
        else:
            self.password = pw
            self.username = un

        # option B:
        # self.username = un
        # self.password = self.set_password(pw)
    
    def get_username(self):
        return self.username
    
    def set_password(self, new_pass):
        if len(new_pass) < 4:
            print("invalid password, it must be at least 4 characters long")
        else: self.password = new_pass


user1 = User ("bob", "123")
user2 = User ("steve", "1234")

user1.set_password("12")