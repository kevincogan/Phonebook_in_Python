from NameNode import NameNode
from NumberNode import NumberNode
from Person import Person

remove_name = False #If the name is not on the tree this value will be called.

#This is the menu for the user to interact with the phonebook.
def menu(NameNode, NumberNode):

    flag = True
    while flag: #Loops untill flag is set to false which is by pressing key 5 when requested to on the menu.
        print("Welcome to the phonebook")
        print("1 - Add Contact")
        print("2 - Get Contact Number By Name")
        print("3 - Get Name And Address By Phone Number")
        print("4 - Remove Contact")
        print("5 - Quit")

        selection = input("Please select a number: ")

        #Option 1, to add contact to phonebook.
        if selection == "1":
            full_name = input("Please enter your full name: ")
            phone_number = input("Please enter your phone number: ")
            address = input("Please enter your address: ")


            details = Person(full_name, phone_number, address) #Makes a Person object.
            NameNode.add_contact_name(details) #Adds to the name binary tree.
            NumberNode.add_contact_number(details) #Adds to the number binary tree.

        #Option 2, gets the number by name.
        elif selection == "2":
            name = input("Who's number would you like to find? ")
            print(NameNode.search_contact_number(name)) #Searches name tree for the name and finds the associated number.

        #Option 3, gets the name and address by phone number.
        elif selection == "3":
            number = input("What is the persons number? ")
            print(NumberNode.search_contact_name_by_number(number)) # Searches the number binary tree for the name and address by using the inputted number.

        #Option 4, remove contact.
        elif selection == "4":
            remove_name = input("What is the name of the contact you would like to remove? ")
            remove_name = NameNode.find_name(remove_name) # Finds the object of the desired name from the name binary tree.

            if remove_name == True: # If name not is not empty.
                print("Phonebook is empty.")

            elif remove_name:
                remove_number = remove_name.get_number() # gets the phone number from the object.
                remove_number = NumberNode.find_number(remove_number) #retieves the number object from the number object tree.

                NameNode.delete_contact_name(NameNode, remove_name) #Deletes the node from the name binary tree.
                NumberNode.delete_contact_number(NumberNode, remove_number) #Deletes the node from the number binary tree.

            else: #If contact is not in the binary tree.
                print("Contact is not in phonebook")

        #Option 5, exit from menu.
        elif selection == "5":
            flag = False


#####################################################################################################


NameNode = NameNode()
NumberNode = NumberNode()

#TEST DATA FOR THE TREE
details = Person("M---", "086---", "-------") # Allows for a even build of the binary tree preventing the chance of a one sided binary tree.
details_2 = Person("Coby", "123", "122 Sicklemore Street")
details_3 = Person("Anna", "0862343233", "Street")
details_4 = Person("Elif", "3", "Some Street")
details_5 = Person("D", "08623233", "Some Street")
NumberNode.add_contact_number(details)
NameNode.add_contact_name(details)
NumberNode.add_contact_number(details_2)
NameNode.add_contact_name(details_2)
NumberNode.add_contact_number(details_3)
NameNode.add_contact_name(details_3)
NumberNode.add_contact_number(details_4)
NameNode.add_contact_name(details_4)
NumberNode.add_contact_number(details_5)
NameNode.add_contact_name(details_5)

menu(NameNode, NumberNode)




#####################################################################################################

# details = Person("Kevin", "1234567", "123 Baker Street")
# details_2 = Person("Tom", "089123234", "122 Sicklemore Street")
#
# #NumberNode.add_contact_number(details)
# #NumberNode.add_contact_number(details_2)
# #print(NumberNode.deletion(details))
#
# NameNode.add_contact_name(details)
# NameNode.add_contact_name(details_2)
# NameNode.find_name("Tom")
# print(NameNode.deletion(details_2))
# print("------------------------------------------------------------------")
# #print(NumberNode.deletion(details_2))
# print(NameNode.deletion(details))
# #NumberNode.print_tree()




#details_2 = Person("Tom", "089123234", "122 Sicklemore Street")
##print(details.get_name())
##print(details.phone_number)
#
#
#root = NameNode()
#root_2 = NumberNode()
#root.add_contact_name(details)
#root.print_tree()
#root.find_name()
#root.add_contact_name(details_2)
#NumberNode.print_tree()
#
#print((root.search_contact_number("Kevin")))
#print(root.search_contact_number("Tom"))
#
#
#print(root_2.search_contact_name_by_number("1234567"))
#print("----------------------------------------------------------------------------------------------------")
#print(root_2.search_contact_name_by_number("089123234"))
