import sys

def add_contact():
    fname = input("First Name: ")
    lname = input("Last Name: ")
    number = input("Phone Number: ")
    with open("contacts.txt", "a") as file:
        file.write(f"{fname},{lname},{number}\n")
    print("Contact added.")


def view_contacts():
    pass

def search_contact():
    pass

def delete_contact():
    pass

def update_contact():
    pass

def sort_contacts():
    pass

def import_contacts():
    pass

def export_contacts():
    pass

def exit():
    sys.exit("Exiting the Contact Book. Goodbye!")