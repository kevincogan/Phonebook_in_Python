# Phonebook Application

## Overview

This repository contains a Python-based **Phonebook Application** that uses binary search trees to efficiently store, search, and manage contact information. The application allows users to perform actions such as adding contacts, retrieving contact details by name or phone number, and deleting contacts.

## Features

1. **Add Contact**: Add a new contact with full name, phone number, and address.
2. **Search by Name**: Retrieve a contact's phone number by providing their name.
3. **Search by Phone Number**: Retrieve a contact's name and address using their phone number.
4. **Delete Contact**: Remove a contact from the phonebook by name.
5. **Binary Search Tree Implementation**:
   - Contacts are stored in two separate binary search trees: one for names and another for phone numbers, ensuring efficient search and management.
6. **Menu-Driven Interface**: Interactive command-line menu for user operations.

## Project Structure

- **NameNode**: Manages the binary search tree for storing and searching contacts by name.
- **NumberNode**: Manages the binary search tree for storing and searching contacts by phone number.
- **Person**: A class that represents a contact, including their name, phone number, and address.
- **menu function**: Provides an interface for user interaction.

## Prerequisites

- Python 3.x

## Installation and Usage

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/kevincogan/Phonebook-Application.git
   cd Phonebook-Application
   ```

2. **Run the Application**:
   ```bash
   python phonebook.py
   ```

3. **Interact with the Menu**:
   - Add, search, or remove contacts as per the displayed options.

## Menu Options

1. **Add Contact**:
   - Prompts the user for name, phone number, and address.
   - Adds the contact to both the name and number binary search trees.

2. **Search by Name**:
   - Prompts the user for a name.
   - Displays the associated phone number if the contact exists.

3. **Search by Phone Number**:
   - Prompts the user for a phone number.
   - Displays the associated name and address if the contact exists.

4. **Remove Contact**:
   - Prompts the user for a name.
   - Deletes the contact from both the name and number binary search trees if the contact exists.

5. **Quit**:
   - Exits the application.

## Example Input and Output

### Adding a Contact
**Input:**
```
1 - Add Contact
Please enter your full name: John Doe
Please enter your phone number: 1234567890
Please enter your address: 123 Elm Street
```

**Output:**
```
Contact added successfully.
```

### Searching for a Contact by Name
**Input:**
```
2 - Get Contact Number By Name
Who's number would you like to find? John Doe
```

**Output:**
```
1234567890
```

### Removing a Contact
**Input:**
```
4 - Remove Contact
What is the name of the contact you would like to remove? John Doe
```

**Output:**
```
Contact removed successfully.
```

## Notes

- The application uses a binary search tree for efficient storage and retrieval of contact information.
- External modules such as `NameNode`, `NumberNode`, and `Person` are required for proper functionality.
- Ensure that all required modules are included in the same directory as the main script.

## Contribution

Contributions are welcome! To contribute:
1. Fork the repository.
2. Create a new branch for your feature or fix.
3. Commit your changes and push them to your fork.
4. Open a pull request describing your changes.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.

---

Enjoy managing your contacts efficiently with this binary-tree-based Phonebook Application!

