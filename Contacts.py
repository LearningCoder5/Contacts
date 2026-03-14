contacts = []

def add_contact(name, phone):
    contact = {
        'name': name,
        'phone': phone
    }
    contacts.append(contact)

def list_contacts():
    for contact in contacts:
        print(f"Name: {contact['name']}, Phone: {contact['phone']}")
    
def find_contact(name):
    for contact in contacts:
        if contact['name'] == name:
            return contact
        
    

def delete_contact(name):
    contact =find_contact(name)
    if contact:
        contacts.remove(contact)
        print("Contact deleted successfully!")
    else:        print("Contact not found.")    
    
    



def main():
    while True:
        print("\nContact Management System\n1. Add Contact\n2. List Contacts\n3. Find Contact\n4. Delete Contact\n5. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            try:
                name = input("Enter name: ")
                phone = int(input("Enter phone number: "))

                if len(str(phone)) != 9:
                    print("Phone number must be 9 digits long.")
                
                else:
                    add_contact(name, phone)
                    print("Contact added successfully!")
                   
            except ValueError:
                print("Invalid input. Please enter a valid phone number.")


        elif choice == '2':
            list_contacts()


        elif choice == '3':
            name = input("Enter name to find: ")
            contact = find_contact(name)
            if contact:
                print(f"Name: {contact['name']}, Phone: {contact['phone']}")
            else:
                print("Contact not found.")


        elif choice == '4':
            name = input("Enter name to delete: ")
            delete_contact(name)

        elif choice == '5':
            break


        else:
            print("Invalid choice. Please try again.")


main()
