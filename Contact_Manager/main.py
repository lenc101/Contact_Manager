import json


contacts = []

menu = {
    "1": "Add contact",
    "2": "View contacts",
    "3": "Search contacts",
    "4": "Edit contact",
    "5": "Delete contact",
    "6": "Save contacts",
    "7": "Load contacts",
    "8": "Exit"
}


def add_contact():
    print("\n" + "=" * 40)
    print("             ADD CONTACT")
    print("=" * 40)

    new_contact = {}

    new_contact["name"] = input("Name: ").strip()
    new_contact["phone"] = input("Phone: ").strip()
    new_contact["email"] = input("Email: ").strip()

    contacts.append(new_contact)

    print("\nContact added successfully!")


def show_menu():
    print("\n" + "=" * 40)
    print("            CONTACT MANAGER")
    print("=" * 40)

    for number, option in menu.items():
        print(f"  {number}. {option}")

    print("=" * 40)

    choice = input("Choose an option: ").strip()
    return choice


def show_contacts():
    print("\n" + "=" * 40)
    print("             CONTACTS")
    print("=" * 40)

    if not contacts:
        print("No contacts found.")
    else:
        for number, contact in enumerate(contacts, start=1):
            print(f"\nContact {number}")
            print("-" * 25)
            print("Name:", contact["name"])
            print("Phone:", contact["phone"])
            print("Email:", contact["email"])

    print("=" * 40)


def search_contact():
    print("\n" + "=" * 40)
    print("           SEARCH CONTACT")
    print("=" * 40)

    found = False
    name = input("Search by name: ").strip()

    for contact in contacts:
        if contact["name"] == name:
            print("\nContact found!")
            print("-" * 25)
            print("Name:", contact["name"])
            print("Phone:", contact["phone"])
            print("Email:", contact["email"])
            found = True

    if not found:
        print("\nContact doesn't exist.")


def edit_contact():
    print("\n" + "=" * 40)
    print("            EDIT CONTACT")
    print("=" * 40)

    found = False
    name = input("Search by name: ").strip()

    for contact in contacts:
        if contact["name"] == name:
            contact["phone"] = input("New phone: ").strip()
            contact["email"] = input("New email: ").strip()
            found = True

            print("\nContact updated successfully!")

    if not found:
        print("\nContact doesn't exist.")


def delete_contact():
    print("\n" + "=" * 40)
    print("           DELETE CONTACT")
    print("=" * 40)

    found = False
    name = input("Search by name: ").strip()

    for contact in contacts:
        if contact["name"] == name:
            contacts.remove(contact)
            found = True

            print("\nContact deleted successfully!")
            break

    if not found:
        print("\nContact doesn't exist.")


def save_contacts():
    with open("contacts.json", "w") as file:
        json.dump(contacts, file, indent=4)

    print("\nContacts saved successfully!")


def load_contacts():
    global contacts

    try:
        with open("contacts.json", "r") as file:
            contacts = json.load(file)

        print("\nContacts loaded successfully!")

    except FileNotFoundError:
        print("\nNo contacts file found.")


def main():
    while True:
        choice = show_menu()

        if choice == "1":
            add_contact()

        elif choice == "2":
            show_contacts()

        elif choice == "3":
            search_contact()

        elif choice == "4":
            edit_contact()

        elif choice == "5":
            delete_contact()

        elif choice == "6":
            save_contacts()

        elif choice == "7":
            load_contacts()

        elif choice == "8":
            print("\nGoodbye!")
            break

        else:
            print("\nInvalid input! Choose 1 - 8.")


main()
