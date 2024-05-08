def process_user_contacts(user_input):
    user_contacts = {}

    user_input = user_input.replace(" ", ",") 

    split_input = user_input.split(',') 
   
    for i in range(0, len(split_input), 2):
        name = split_input[i]                   
        phone_number = split_input[i + 1]      
        user_contacts[name] = phone_number      
    
    contact_name = input("Enter the contact name: ")
    if contact_name in user_contacts:
        print(user_contacts[contact_name])         
    else:
        print("Contact not found.")
    
   
if __name__ == '__main__':
    # Get input for word pairs
    user_input = input("Enter word pairs (name, phone number): ")

    # Call the function to process user contacts
    process_user_contacts(user_input)
