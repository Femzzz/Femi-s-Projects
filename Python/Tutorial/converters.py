import random
def lbs_to_kg(weight):
    return weight * 0.45


def kg_to_lbs(weight):
    return weight / 0.45


def find_max(numbers):
    maximum = numbers[0]
    for number in numbers:
        if number > maximum:
            maximum = number
    return maximum


def emoji_converter(message):
    words = message.split(" ")
    emojis = {
        ":)": "😊",
        ":(": "😢",
        ":D": "😄",
        ";)": "😉",
        ":P": "😛"
    }
    output = ""
    for word in words: 
        output += emojis.get(word, word) + " "
    return output  


class Mammal:
    def walk(self):
        print("walk")


class Dog(Mammal):
    def bark(self):
        print("woof")


class Cat(Mammal):
    def be_annoying(self):
        print("annoying")


class Person(Mammal):
    # constructor
    def __init__(self, name):
        self.name =  name
    def talk(self):
        print(f"I am {self.name}")


class Dice:
    def roll(self):
        for i in range(1):
            values = f"({random.randint(1, 6)}, {random.randint(1, 6)})"
            print(values)

