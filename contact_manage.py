import json
import os

CONTACTS_FILE = "contacts.json"

def load_contacts():
    """Load contacts from the file."""
    if os.path.exists(CONTACTS_FILE):
        with open(CONTACTS_FILE, "r") as file:
            return json.load(file)
    return []

def save_contacts(contacts):
    """Save contacts to the file."""
    with open(CONTACTS_FILE, "w") as file:
        json.dump(contacts, file, indent=4)

def add_contact():
    """Add a new contact."""
    name = input("Enter Name: ").strip()
    phone = input("Enter Phone Number: ").strip()
    email = input("Enter Email: ").strip()

    contacts = load_contacts()
    contacts.append({"name": name, "phone": phone, "email": email})
    save_contacts(contacts)
    print("\n✅ Contact Added Successfully!")

def view_contacts():
    """Display all contacts."""
    contacts = load_contacts()
    if not contacts:
        print("\n📂 No Contacts Found!")
        return
    
    print("\n📋 Contact List:")
    for i, contact in enumerate(contacts, start=1):
        print(f"{i}. {contact['name']} | {contact['phone']} | {contact['email']}")

def edit_contact():
    """Edit an existing contact."""
    contacts = load_contacts()
    if not contacts:
        print("\n📂 No Contacts to Edit!")
        return
    
    view_contacts()
    try:
        index = int(input("\nEnter Contact Number to Edit: ")) - 1
        if 0 <= index < len(contacts):
            contacts[index]["name"] = input("Enter New Name: ").strip()
            contacts[index]["phone"] = input("Enter New Phone: ").strip()
            contacts[index]["email"] = input("Enter New Email: ").strip()
            save_contacts(contacts)
            print("\n✅ Contact Updated Successfully!")
        else:
            print("\n❌ Invalid Contact Number!")
    except ValueError:
        print("\n❌ Please Enter a Valid Number!")

def delete_contact():
    """Delete a contact."""
    contacts = load_contacts()
    if not contacts:
        print("\n📂 No Contacts to Delete!")
        return
    
    view_contacts()
    try:
        index = int(input("\nEnter Contact Number to Delete: ")) - 1
        if 0 <= index < len(contacts):
            deleted_contact = contacts.pop(index)
            save_contacts(contacts)
            print(f"\n🗑️ Contact '{deleted_contact['name']}' Deleted Successfully!")
        else:
            print("\n❌ Invalid Contact Number!")
    except ValueError:
        print("\n❌ Please Enter a Valid Number!")

def main():
    """Main function to run the contact management system."""
    while True:
        print("\n📞 Contact Management System")
        print("1️⃣ Add Contact")
        print("2️⃣ View Contacts")
        print("3️⃣ Edit Contact")
        print("4️⃣ Delete Contact")
        print("5️⃣ Exit")

        choice = input("Enter Your Choice (1-5): ").strip()

        if choice == "1":
            add_contact()
        elif choice == "2":
            view_contacts()
        elif choice == "3":
            edit_contact()
        elif choice == "4":
            delete_contact()
        elif choice == "5":
            print("\n👋 Exiting... Thank You!")
            break
        else:
            print("\n❌ Invalid Choice! Please Enter a Number Between 1-5.")

# Run the program
main()
