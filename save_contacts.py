import csv

def save_contacts(all_contacts):
    #print('All Conntacts : ', all_contacts)
    #input()
    with open('all_contacts.csv', 'w', newline='') as csvfile:
        fieldnames = ['name', 'email', 'mobile', 'gender', 'address']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(all_contacts)


