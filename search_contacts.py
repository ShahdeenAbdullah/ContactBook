
import csv

def search_contacts():

    try:
        search_value = input("Enter Mobile Number to search: ")

        with open('all_contacts.csv', mode="r") as file:

            reader = csv.DictReader(file)
            # Use DictReader for easier column access
            for row in reader:
                if row["mobile"] == search_value:
                    print("Found:", row)
                    break
            else:
                print("Item not found.")

    except ValueError:
        print("System Not working! Please wait a while........")
