import converters
from converters import Cat, Dog, Mammal, Person
from converters import emoji_converter, find_max


john = Person("femi")
john.talk()

convert = input("> ")
print(emoji_converter(convert))
