#IMPORTING
import csv
import os
import re
from termcolor import colored


#FUNCTIONS
def create_new(book):
    """This function creates new contact book. It takes one positional argument [name of the book]"""
    with open(book,"w",newline="") as csvfile:
        fieldnames=["Last Name", "First name", "Phone number", "Mail", "Address"]
        writer = csv.DictWriter(csvfile,fieldnames=fieldnames)
        writer.writeheader()

def create_entry(book):
    """This function creates new entry in given contact book. It takes one positional argument [name of the book]"""
    with open(book,"a",newline="") as csvfile:
        fieldnames=["Last Name", "First name", "Phone number", "Mail", "Address"]
        writer = csv.DictWriter(csvfile,fieldnames=fieldnames)
        writer.writerow({"Last Name":input("Please, provide last name for the contact: "), "First name":input("Please, provide first name for the contact: "), "Phone number":input("Please, provide phone number for the contact: "), "Mail":input("Please, provide email address for the contact: "), "Address":input("Please, provide address for the contact: ")})

def look_for(book,contact):
    """This function look for given info in given contact book. It takes two positional argument [name of the book] and [info]"""
    with open(book,"r",newline="") as csvfile:
        fieldnames=["Last Name", "First name", "Phone number", "Mail", "Address"]
        reader = csv.DictReader(csvfile,fieldnames=fieldnames)
        next(reader, None)
        for row in reader:
            lname,fname,phone,mail,address=row
            pattern=contact
            result=re.search(pattern,str(row),re.IGNORECASE)
            if result!=None:
                print(colored("Last Name:","yellow"), row['Last Name'],colored(" First name:","yellow"), row['First name'],colored(" Phone number:","yellow"), row['Phone number'],colored(" Mail:","yellow"), row['Mail'],colored(" Address:","yellow"), row['Address'])

def show_book(book):
    """This function shows contact book. It takes one positional argument [name of the book]"""
    with open(book,"r",newline="") as csvfile:
        fieldnames=["Last Name", "First name", "Phone number", "Mail", "Address"]
        reader = csv.DictReader(csvfile,fieldnames=fieldnames)
        next(reader, None)
        for row in reader:
            #print(f"{row.key()}: {row.value()}")
            #print(dict(row))
            print(colored("Last Name:","yellow"), row['Last Name'],colored(" First name:","yellow"), row['First name'],colored(" Phone number:","yellow"), row['Phone number'],colored(" Mail:","yellow"), row['Mail'],colored(" Address:","yellow"), row['Address'])
            #, , "Phone number: ","yellow", row['Phone number'], "Mail: ","yellow", row['Mail'], "Address: ","yellow", row['Address']))

#CODE
print("Wlecome in your contact book manager :)\n")
while True:
    decision=int(input("Choose action from menu.\nInput only a number corresponding to the position\n1. Create new contact book\n2. Open existing contact book\n3. Create new entry to existing contact book\n4. Look for data in book\n\nChoosed option: "))
    if decision==1:
        name=input("\nHow would you like to name your new contact book?: ")
        create_new(name)
    elif decision==2:
        filenames = next(os.walk(os.getcwd()), (None, None, []))[2]  # [] if no file
        position=1
        print("\nChoose action from menu.\nInput only a number corresponding to the position")
        filenames.remove("contact_book.py")
        print (filenames)
        for i in filenames:
            print (position, ". ",i)
            position+=1
        index=int(input("\nChoosed option: "))-1
        option=filenames[index]
        try:
            show_book(option)
        except:
            print ("Please, provide correct answer\n")
    elif decision==3:
        filenames = next(os.walk(os.getcwd()), (None, None, []))[2]  # [] if no file
        filenames.remove("contact_book.py")
        position=1
        print("\nWelcome in new entry creator!\nWitch book do you want to append?\n\nChoose action from menu.\nInput only a number corresponding to the position")
        for i in filenames:
            print (position, ". ",i)
            position+=1
        index=int(input("\nChoosed option: "))-1
        option=filenames[index]
        create_entry(option)
    elif decision==4:
        filenames = next(os.walk(os.getcwd()), (None, None, []))[2]  # [] if no file
        filenames.remove("contact_book.py")
        position=1
        print("\nWelcome! Lets start searching\nWitch book should be searched?\n\nChoose action from menu.\nInput only a number corresponding to the position")
        for i in filenames:
            print (position, ". ",i)
            position+=1
        index=int(input("\nChoosed option: "))-1
        option=filenames[index]
        contact=input("What info are we looking for?: ")
        look_for(option,contact)
    else:
        print ("Please, provide correct answer\n")
