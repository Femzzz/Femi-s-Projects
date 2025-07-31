import contact_functions
from os import path
from contact_functions import add_contact
#Contact Book

path = r"C:\Users\abxy3\OneDrive\Документы\Python\Femi's Projects\Contact Book\contacts.txt"

function = 0

while function < 1:
    command = input("Choose A command:(Add,View,Update,Search,Delete,Exit): ").lower()
    if command == "add":
        add_contact()
    else:
        pass
        
open(path, "a").close()  # Create the file if it doesn't exist 

