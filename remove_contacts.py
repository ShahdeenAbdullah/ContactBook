
def remove_contacts(all_contacts):
    try:

        if not all_contacts:
            print("Contact Book is empty")
            return all_contacts
        delete_contact = input("Enter the deleting Mobile Number: ")
        for contacts in all_contacts:
            if str(contacts['mobile']) == delete_contact:
                all_contacts.remove(contacts)
                print(f"Mobile Number {delete_contact} has been removed")
                return all_contacts
        print("No such mobile number")
        return all_contacts
    except ValueError:
        print("System not working! Please wait a while.")