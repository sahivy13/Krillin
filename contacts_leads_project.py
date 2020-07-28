import json
from os import listdir
from os.path import isfile, join
import pickle

# Creating list of JSON file paths

json_database_dir_name = "registrant_form_log"
json_fp_list = [join(json_database_dir_name, f) for f in listdir(json_database_dir_name) if
                isfile(join(json_database_dir_name, f))]


# Creating class for registrant object

class Registrant():
    def __init__(self, name, email, phone):
        self.name = name
        self.email = email
        self.phone = phone


# creating lists of Contacts and Leads with information of people already in database

try:
    with open('ContactList.obj', 'rb') as f:
        ContactList = pickle.load(f)
    with open('ContactList.obj', 'rb') as f:
        LeadsList = pickle.load(f)

except:
    ContactsList = [
        Registrant("Alice Brown", "None", "1231112223"),
        Registrant("Bob Crown", "bob@crowns.com", "None"),
        Registrant("Carlos Drew", "carl@drewess.com", "3453334445"),
        Registrant("Doug Emerty", "None", "4564445556"),
        Registrant("Egan Fair", "eg@fairness.com", "5675556667")
    ]

    LeadsList = [
        Registrant("None", "kevin@keith.com", "None"),
        Registrant("Lucy", "lucy@liu.com", "None"),
        Registrant("Mary Middle", "mary@middle.com", "3331112223"),
        Registrant("None", "None", "4442223334"),
        Registrant("None", "ole@olson.com", "None")
    ]


# Creating main function

def read_Reg_Form(
        json_file):  # json_file is the location of the file with the file name, if in local directory then it is just the name of the file.
    with open(json_file) as f:
        form_data = json.load(f)

    form_name = form_data['registrant']['name']
    form_email = form_data['registrant']['email']
    form_phone = form_data['registrant']['phone']

    def check_Update_Or_Add(reg_name, reg_email, reg_phone):  # This function checks the list

        print('Checking contact list')

        for contact in ContactsList:
            if contact.email == reg_email:
                if contact.phone == "None":
                    print(f"Upadting phone number of contact: {contact.name}")
                    contact.phone = reg_phone
                    break
                else:
                    print("Contact already in contact list with same info")
                    break
            elif contact.phone == reg_phone:
                if contact.email == "None":
                    print(f"Upadting email number of contact: {contact.name}")
                    contact.email = reg_email
                    break
                else:
                    print("Contact already in contact list with same info")
                    break
            elif contact == ContactsList[-1]:
                print("Registration form contact is not in contacts list...")
                print("Now checking lead list")
                for lead in LeadsList:
                    if lead.email == reg_email:
                        if lead.phone == "None":
                            print(f"Upadting phone number of lead: {lead.name}")
                            lead.phone = reg_phone
                            res = ContactsList.insert(LeadsList.index(lead), LeadsList.pop(LeadsList.index(lead)))
                            break
                    elif lead.phone == reg_phone:
                        if lead.email == "None":
                            print(f"Upadting email number of lead: {lead.name}")
                            lead.email = reg_email
                            res = ContactsList.insert(LeadsList.index(lead), LeadsList.pop(LeadsList.index(lead)))
                            break
                    else:
                        print("Registration form contact is not in leads list...")
                        print("Adding contact to contacts list")
                        ContactsList.append(Registrant(reg_name, reg_email, reg_phone))

    check_Update_Or_Add(form_name, form_email, form_phone)
    print("Done!")


for p in json_fp_list:
    read_Reg_Form(p)

print("Current contact list is:")
for i in ContactsList:
    print("-----")
    print(f"Name: {i.name}, Email: {i.email}, Phone Number: {i.phone}")
print(".......")
print("Current lead list is:")
for i in LeadsList:
    print("-----")
    print(f"Name: {i.name}, Email: {i.email}, Phone Number: {i.phone}")

with open('ContactList', 'wb') as f:
    pickle.dump(ContactsList, f)

with open('LeadsList', 'wb') as f:
    pickle.dump(LeadsList, f)
