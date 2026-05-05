# Class 1 -- Playlist Class:
print("====== Class 1 -- Playlist Class: =====")
class Playlist:
    def __init__(self, name, song_count = 1):
        self.name = name
        self.song_count = song_count

    def add_song(self):
        self.song_count += 1

    def remove_song(self):
        if self.song_count == 0:
            print("There are no more songs in the playlist")
        else:
            self.song_count -= 1

    def show_info(self):
        print(f"Playlist '{self.name}' has {self.song_count} songs in it.")

playlist1 = Playlist("Favourites")
playlist1.show_info()
playlist1.add_song()
playlist1.add_song()
playlist1.remove_song()

playlist1.show_info()


# Class 2 -- Shopping Cart:
print("====== Class 2 -- ShoppingCart Class: =======")
class ShoppingCart:
    def __init__(self, owner, item_count):
        self.owner = owner
        self.item_count = item_count
    
    def add_item(self, quantity):
        self.item_count += quantity

    def remove_item(self, quantity):
        if quantity > self.item_count:
            print("You can't remove more items than you have in the cart")
        else:
            self.item_count -= quantity
    
    def show_cart(self):
        print(f"Owner {self.owner} has {self.item_count} items in the cart")

cart1 = ShoppingCart("Jane", 3)
cart1.show_cart()
cart1.add_item(2)
cart1.remove_item(6)
cart1.remove_item(1)
cart1.show_cart()

# Class 3 -- User Accoubnt:
print("====== Class 3 -- User Account: =======")
class UserAccount:
    def __init__(self, username, login_count = 0, active = False):
        self.username = username
        self.login_count = login_count
        self.active = active

    def activate(self):
        if self.active == True:
            print(f"The user {self.username} is already active")
        else:
            self.active = True
            print(f"The user {self.username} is successfully activated")

    def deactivate(self):
        if self.active == False:
            print(f"The user {self.username} is already deactivated")
        else:
            self.active = False
            print(f"The user {self.username} is successfully deactivated")

    def login(self):
        if self.active == False:
            print(f"User {self.username} should be activated before loggin in.")
        else:
            self.login_count += 1

    def show_status(self):
        if self.active == True: status = "active"
        else: status = "deactivated"
        print(f"{self.username} has logged in {self.login_count} times and has status: {status}.")

user1 = UserAccount("Bob")
user1.show_status()
user1.login()
user1.activate()
user1.login()
user1.login()
user1.show_status()
user1.deactivate()
user1.show_status()




        

