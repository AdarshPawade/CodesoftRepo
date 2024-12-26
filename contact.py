# Contact Management System
contacts = {}

def add_contact():
    name = input("Enter name: ").strip()
    if name in contacts:
        print("Contact with this name already exists!")
        return

    phone = input("Enter phone number: ").strip()
    email = input("Enter email: ").strip()
    address = input("Enter address: ").strip()

    contacts[name] = {"phone": phone, "email": email, "address": address}
    print(f"Contact {name} added successfully!")

def view_contacts():
    if not contacts:
        print("No contacts available.")
        return

    print("\nContact List:")
    for name, details in contacts.items():
        print(f"Name: {name}, Phone: {details['phone']}")
    print()

def search_contact():
    query = input("Enter name or phone number to search: ").strip()
    found = False

    for name, details in contacts.items():
        if query.lower() in name.lower() or query in details["phone"]:
            print(f"\nContact Found:")
            print(f"Name: {name}")
            print(f"Phone: {details['phone']}")
            print(f"Email: {details['email']}")
            print(f"Address: {details['address']}")
            found = True

    if not found:
        print("No contact found with the given details.")

def update_contact():
    name = input("Enter the name of the contact to update: ").strip()
    if name not in contacts:
        print("Contact not found!")
        return

    print("\nUpdate Contact:")
    phone = input("Enter new phone number (leave blank to keep current): ").strip()
    email = input("Enter new email (leave blank to keep current): ").strip()
    address = input("Enter new address (leave blank to keep current): ").strip()

    if phone:
        contacts[name]["phone"] = phone
    if email:
        contacts[name]["email"] = email
    if address:
        contacts[name]["address"] = address

    print(f"Contact {name} updated successfully!")

def delete_contact():
    name = input("Enter the name of the contact to delete: ").strip()
    if name not in contacts:
        print("Contact not found!")
        return

    del contacts[name]
    print(f"Contact {name} deleted successfully!")

def contact_manager():
    print("Welcome to Contact Management System!")
    while True:
        print("\nMenu:")
        print("1. Add Contact")
        print("2. View Contact List")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ").strip()

        if choice == "1":
            add_contact()
        elif choice == "2":
            view_contacts()
        elif choice == "3":
            search_contact()
        elif choice == "4":
            update_contact()
        elif choice == "5":
            delete_contact()
        elif choice == "6":
            print("Exiting Contact Management System. Goodbye!")
            break
        else:
            print("Invalid choice! Please select a valid option.")

if __name__ == "__main__":
    contact_manager()
