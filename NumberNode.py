from Person import Person
class NumberNode:

	def __init__(self, phone_number=None):

		self.left = None
		self.right = None
		self.phone_number = phone_number

#Creates a binary search tree with person objects and ordered with contact numbers
	def add_contact_number(self, phone_number):

		#Checks if phone_number has a value of None.
		if self.phone_number == None:
			self.phone_number = phone_number

		else:
			if phone_number.get_number() > (self.phone_number).get_number(): # If name is greater than current node.
				if self.right: #Checks if there is a right node.
					self.right.add_contact_number(phone_number) #recursively seaches right.
				else:
					self.right = NumberNode(phone_number) #creates a new object with the values.

			elif phone_number.get_number() < (self.phone_number).get_number(): #If name is less than current node.
				if self.left:
					self.left.add_contact_number(phone_number)
				else:
					self.left = NumberNode(phone_number)


# search_contact method to compare the value with nodes
	def search_contact_name_by_number(self, contact_info):

		if self.phone_number.get_number() == "086---" and self.left == None and self.right == None: #Checks if it is equal to the balancer and if the right anf left nodes of the balancer are empty.
			return "No contacts in the phonebook"

		elif self.phone_number.get_number() == contact_info:
			return (str(self.phone_number.get_name()) + " - " + str(self.phone_number.get_address()))

		#Recursively searches through the tree moving left or right depending if the value is grater or less that the current node.
		elif contact_info < (self.phone_number).get_number() and self.left is not None:
			return self.left.search_contact_name_by_number(contact_info)


		elif contact_info > (self.phone_number).get_number() and self.right is not None:
			return self.right.search_contact_name_by_number(contact_info)

		else:
			return str(contact_info) + "'s contact information was not found"


	def find_number(self, contact_name):

		#Desired node is found
		if self.phone_number.get_number() == contact_name:
			return self.phone_number

		#Recursively searches through the tree moving left or right depending if the value is grater or less that the current node.
		elif contact_name < self.phone_number.get_number() and self.left is not None:
			return self.left.find_number(contact_name)
		elif contact_name > self.phone_number.get_number() and self.right is not None:
			return self.right.find_number(contact_name)


	#This deletes nodes in a binary tree.
	def delete_contact_number(self, number_node , contact_info):

		#Recursively searches through the tree moving left or right depending if the value is grater or less that the current node.
		if contact_info.get_number() < number_node.phone_number.get_number():
			number_node.left = self.delete_contact_number(number_node.left, contact_info)

		elif contact_info.get_number() > number_node.phone_number.get_number():
			number_node.right = self.delete_contact_number(number_node.right, contact_info)

		#If desired node is found.
		else:

			#If the parent node has no children.
			if number_node.left == None and number_node.right == None:
				if self.phone_number.get_number() == number_node.phone_number.get_number():
					pass

				else:
					number_node = None

			#If the parent node only has one child node.
			elif number_node.left == None or number_node.right == None:
				if number_node.left == None: # If child node is right.

					if self.phone_number == number_node.phone_number:
						pass
					else:
						number_node = number_node.right

				elif number_node.right == None: # If child node is left.
					if self.phone_number.right == number_node.phone_number:
						pass
					else:
						number_node = number_node.left

			#If the parent node has two children
			elif number_node.left != None and number_node.right != None:

				reconnect_node = number_node.right
				while reconnect_node.left != None: # FInd the most left node.
					reconnect_node = reconnect_node.left

				number_node.phone_number = reconnect_node.phone_number #Connects to the current tree.
				number_node.right = self.delete_contact_number(number_node.right, reconnect_node.phone_number)
		return number_node
