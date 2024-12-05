
import csv
def load_contacts():
    try:
        with open("all_contacts.csv", mode="r") as mycontacts:
            reader = csv.DictReader(mycontacts)
            return [contacts for contacts in reader]
    except FileNotFoundError:
        return []



