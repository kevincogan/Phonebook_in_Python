from Person import Person
class NameNode:

	def __init__(self, name = None):

		self.name = name
		self.left = None
		self.right = None

#Creates a binary search tree with person objects and ordered with contact names.
	def add_contact_name(self, name):

		#Checks if phone_number has a value of None.
		if self.name == None:
			self.name = name

		else:
			if name.get_name() > (self.name).get_name(): # If name is greater than current node.
				if self.right: #Checks if there is a right node.
					self.right.add_contact_name(name)  #recursively seaches right.
				else:
					self.right = NameNode(name) #creates a new object with the values.

			elif name.get_name() < (self.name).get_name(): #If name is less than current node.
					if self.left: #Checks if there is a left node.
						self.left.add_contact_name(name) #recursively seaches left.
					else:
						self.left = NameNode(name) #creates a new object with the values.


# search_contact method to find the number associated with the inputted name.
	def search_contact_number(self, contact_info):

		if self.name.get_name() == "M---" and self.left == None and self.right == None: #Checks if it is equal to the balancer and if the right anf left nodes of the balancer are empty.
			return "No contacts in the phonebook"

		elif self.name.get_name() == contact_info: #if contact is found.
			return (str(self.name.get_number()) + ' is ' + str(contact_info) + "'s phone number")

		#Recursively searches through the tree moving left or right depending if the value is grater or less that the current node.
		elif contact_info < (self.name).get_name() and self.left is not None:
			return self.left.search_contact_number(contact_info)

		elif contact_info > (self.name).get_name() and self.right is not None:
			return self.right.search_contact_number(contact_info)

		else:
			return str(contact_info) + "'s phone number was not found"


	def find_name(self, contact_name):

		#Checks to see if the tree is empty
		if self.name.get_name() == "M---" and self.left == None and self.right == None:
			return True

		#Desired node is found
		elif self.name.get_name() == contact_name:
			return self.name

		#Recursively searches through the tree moving left or right depending if the value is grater or less that the current node.
		elif contact_name < self.name.get_name() and self.left is not None:
			return self.left.find_name(contact_name)

		elif contact_name > self.name.get_name() and self.right is not None:
			return self.right.find_name(contact_name)


	#This deletes the nodes in a binary tree.
	def delete_contact_name(self, name_node , contact_info):

		#Recursively searches through the tree moving left or right depending if the value is grater or less that the current node.
		if contact_info.get_name() < name_node.name.get_name():
			name_node.left = self.delete_contact_name(name_node.left, contact_info)

		elif contact_info.get_name() > name_node.name.get_name():
			name_node.right = self.delete_contact_name(name_node.right, contact_info)

		#If desired node is found.
		else:
			#If the parent node has no children.
			if name_node.left == None and name_node.right == None:

				#If name is equal to the root node.
				if self.name.get_name() == name_node.name.get_name():
					print("Error - Cannot delete system balancer")

				else:
					name_node = None



			#If the parent node only has one child node.
			elif name_node.left == None or name_node.right == None:
				if name_node.left == None: # If child node is right.

					if self.name == name_node.name: #if equal to root node.
						print("Error - Cannot delete system balancer.")

					else:
						name_node = name_node.right #Connects node to current tree.

				elif name_node.right == None: # If child node is left.
					if self.name == name_node.name:
						print("Error - Cannot delete system balancer.")

					else:
						name_node = name_node.left #Connects node to current tree.

			#If the parent node has two children
			elif name_node.left != None and name_node.right != None:

				reconnect_node = name_node.right
				while reconnect_node.left != None: # FInd the most left node.
					reconnect_node = reconnect_node.left

				name_node.name = reconnect_node.name #Connects to the current tree.
				name_node.right = self.delete_contact_name(name_node.right, reconnect_node.name)

		return name_node
