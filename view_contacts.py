
def view_contacts(all_contacts):
    if all_contacts !=[]:
        for contacts in all_contacts:
            print(f"Name:{contacts['name']} | Email:{contacts['email']} | Mobile:{contacts['mobile'] } | Gender:{contacts['gender'] } | Address:{contacts['address']}")

        else:
            print("No Entry Found")



