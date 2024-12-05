from add_contacts import add_contacts
from save_contacts import save_contacts
from view_contacts import view_contacts
from load_contacts import load_contacts
from search_contacts import search_contacts
from remove_contacts import remove_contacts

all_contacts = load_contacts()

while True:
    print("\n Welcome to Contact Names")
    print("0. EXIT")
    print("1. ADD NAME")
    print("2. VIEW ALL NAMES")
    print("3. SEARCH NAME")
    print("4. REMOVE NAME")

    option = input("Choose your option: 0/1/2/3/4: ")

    if option == "0":
        save_contacts(all_contacts)
        print("Thanks for using Contact management")
        break
    elif option == "1":
        all_contacts = add_contacts(all_contacts)

    elif option == "2":
        view_contacts(all_contacts)

    elif option == "3":
        search_contacts()

    elif option == "4":
        remove_contacts(all_contacts)
    else:
        print("Choose the right option")

