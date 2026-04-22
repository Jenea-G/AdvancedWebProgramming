# CONCATINATION

Comma will add one space automatically while + will concatinate without a space.
- Three possible ways to concatinate:

```python
name = "Jane"

print("Hello", self.name, "!")
print("Hello " + self.name + " !")
print(f"Hello {self.name} !") # f"" is like `` in js
```

# CLASS

To create a class:
1) name it: class Name:
2) add initialisation function with arguments
3) add methods if needed

```python
class Friend:
    def __init__(self, name, last_name, age, hobby, music = "none"): # constructor
        self.name = name
        self.last_name = last_name
        self.age = age
        self.hobby = hobby
        self.music = music
        self.full_name = name + " " + last_name

    def print_info(self): # method
        print(self.full_name, self.age, self.hobby, self.music)

f1 = Friend("Bay", "Leaf", 23, "cooking") # f1 is a variable representing an instance of an object
```