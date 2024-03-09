def process_user_contacts(user_input):
    user_contacts = user_input
    tokens = user_contacts.split()

    # Get contact name from input, output contact's phone number
    contact_name = input("Enter the contact name: ")
    
    for i in range (len(tokens)):
        if(tokens[i] == contact_name):
            print(tokens[i+1])
   
if __name__ == '__main__':
    # Get input for word pairs
    user_input = input("Enter word pairs (name, phone number): ")

    # Call the function to process user contacts
    process_user_contacts(user_input)
