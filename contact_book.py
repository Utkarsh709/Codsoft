import json

# Contact management class
class ContactManager:
    def __init__(self, file_path="contacts.json"):
        self.file_path = file_path
        self.contacts = self.load_contacts()

    def load_contacts(self):
        try:
            with open(self.file_path, "r") as file:
                return json.load(file)
        except FileNotFoundError:
            return {}
        except json.JSONDecodeError:
            return {}

    def save_contacts(self):
        try:
            with open(self.file_path, "w") as file:
                json.dump(self.contacts, file, indent=4)
        except PermissionError:
            print(f"Permission denied: Unable to write to {self.file_path}")

    def add_contact(self, name, phone, email):
        self.contacts[name] = {"phone": phone, "email": email}
        self.save_contacts()

    def update_contact(self, name, phone, email):
        if name in self.contacts:
            self.contacts[name] = {"phone": phone, "email": email}
            self.save_contacts()

    def delete_contact(self, name):
        if name in self.contacts:
            del self.contacts[name]
            self.save_contacts()

    def search_contact(self, query):
        results = {}
        for name, details in self.contacts.items():
            if query.lower() in name.lower() or query in details["phone"]:
                results[name] = details
        return results

# Command-line interface class
class ContactManagerCLI:
    def __init__(self, contact_manager):
        self.contact_manager = contact_manager

    def add_contact(self):
        name = input("Enter name: ")
        phone = input("Enter phone: ")
        email = input("Enter email: ")
    
        self.contact_manager.add_contact(name, phone, email)
        print(f"Added contact: {name}")

    def update_contact(self):
        name = input("Enter name: ")
        phone = input("Enter new phone: ")
        email = input("Enter new email: ")
        self.contact_manager.update_contact(name, phone, email)
        print(f"Updated contact: {name}")

    def delete_contact(self):
        name = input("Enter name: ")
        self.contact_manager.delete_contact(name)
        print(f"Deleted contact: {name}")

    def search_contact(self):
        query = input("Enter name or phone to search: ")
        results = self.contact_manager.search_contact(query)
        if results:
            for name, details in results.items():
                print(f"Name: {name}, Phone: {details['phone']}, Email: {details['email']}")
        else:
            print("No contacts found.")

    def display_contacts(self):
        contacts = self.contact_manager.contacts
        if contacts:
            for name, details in contacts.items():
                print(f"Name: {name}, Phone: {details['phone']}, Email: {details['email']}")
        else:
            print("No contacts available.")

    def menu(self):
        while True:
            print("\nContact Manager")
            print("1. Add Contact")
            print("2. Update Contact")
            print("3. Delete Contact")
            print("4. Search Contact")
            print("5. Display All Contacts")
            print("6. Exit")
            choice = input("Enter your choice: ")

            if choice == "1":
                self.add_contact()
            elif choice == "2":
                self.update_contact()
            elif choice == "3":
                self.delete_contact()
            elif choice == "4":
                self.search_contact()
            elif choice == "5":
                self.display_contacts()
            elif choice == "6":
                break
            else:
                print("Invalid choice. Please try again.")

if __name__ == "__main__":
    contact_manager = ContactManager(file_path="contacts.json")
    app = ContactManagerCLI(contact_manager)
    app.menu()

