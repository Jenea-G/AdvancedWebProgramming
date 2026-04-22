# cteate a new class for a friend

# take in 4-5 arguments and initialize it.
# create a function that shows full informnation

class Friend:
    def __init__(self, name, last_name, age, hobby, music):
        self.name = name
        self.last_name = last_name
        self.age = age
        self.hobby = hobby
        self.music = music
        self.full_name = name + " " + last_name

    def print_info(self):
        print(self.full_name, self.age, self.hobby, self.music)

    def greet(self):
        # print("Hello", self.name, "!")
        # print("Hello " + self.name + " !")
        print(f"Hello {self.name} !")

# create 3 instances
friend1 = Friend("Yana", "Mulin", 37, "guitar", "folk")
friend2 = Friend("Peter", "Bush", 40, "hiking", "rock")
friend3 = Friend("Sonya", "Creek", 28, "painting", "electro")

friend1.greet()
friend2.greet()
friend3.greet()