class Person:

    def __init__(self, name = None, phone_number = None, address = None):
        self.name = name
        self.phone_number = phone_number
        self.address = address

    #Retrieves the name from the object.
    def get_name(self):
        return self.name

    #Retrieves the phone number from the object.
    def get_number(self):
        return self.phone_number

    #Retrieves the adress front the object.
    def get_address(self):
        return self.address
