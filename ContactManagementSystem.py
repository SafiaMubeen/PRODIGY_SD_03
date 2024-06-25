import json

contacts = []


def add_contact(name, phone, email):
    contacts.append({"name": name, "phone": phone, "email": email})


def view_contacts():
    for contact in contacts:
        print(f"Name: {contact['name']}, Phone: {contact['phone']}, Email: {contact['email']}")


def edit_contact(name, new_name, new_phone, new_email):
    for contact in contacts:
        if contact["name"] == name:
            contact["name"] = new_name
            contact["phone"] = new_phone
            contact["email"] = new_email
            print("Contact updated successfully.")
            return
    print("Contact not found.")


def delete_contact(name):
    for contact in contacts:
        if contact["name"] == name:
            contacts.remove(contact)
            print("Contact deleted successfully.")
            return
    print("Contact not found.")


def save_contacts(filename):
    with open(filename, "w") as file:
        json.dump(contacts, file)
    print("Contacts saved to file.")


def load_contacts(filename):
    global contacts
    try:
        with open(filename, "r") as file:
            contacts = json.load(file)
        print("Contacts loaded from file.")
    except FileNotFoundError:
        print("No saved contacts found.")


def main():
    filename = "contacts.json"
    load_contacts(filename)

    while True:
        print("\nContact Management System")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Edit Contact")
        print("4. Delete Contact")
        print("5. Save Contacts to File")
        print("6. Load Contacts from File")
        print("7. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Enter name: ")
            phone = input("Enter phone: ")
            email = input("Enter email: ")
            add_contact(name, phone, email)
        elif choice == "2":
            view_contacts()
        elif choice == "3":
            name = input("Enter the name of the contact to edit: ")
            new_name = input("Enter new name: ")
            new_phone = input("Enter new phone: ")
            new_email = input("Enter new email: ")
            edit_contact(name, new_name, new_phone, new_email)
        elif choice == "4":
            name = input("Enter the name of the contact to delete: ")
            delete_contact(name)
        elif choice == "5":
            save_contacts(filename)
        elif choice == "6":
            load_contacts(filename)
        elif choice == "7":
            save_contacts(filename)
            break
        else:
            print("Invalid choice. Please try again.")


main()
