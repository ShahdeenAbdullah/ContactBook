from save_contacts import save_contacts
import csv

def add_contacts(all_contacts):
    name = input("NAME: ")
    email = input("EMAIL: ")
    mobile = input("MOBILE:")
    gender = input("GENDER: ")
    address = input("ADDRESS: ")

    contacts = {
        "name" : name,
        "email" : email,
        "mobile" : mobile,
        "gender" : gender,
        "address" : address
    }
    #print(contacts)
    #input('=---------------')
    all_contacts.append(contacts)
    save_contacts(all_contacts)

    print("Contact added successfully")
    return all_contacts


