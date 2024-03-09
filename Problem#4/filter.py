def process_and_print(input_string):
      # Split into separate strings
    tokens = user_input.split()
    # Convert strings to integers and filter out negative values
    data = []
    for i in range (len(tokens) ):
        if (int(tokens[i]) < 0):
          data.append(int(tokens[i]))
        

    # Sort integers in reverse order
    data.sort(reverse = True)
    # Print sorted integers
    string = ""
    for i in range(len(data) ):
      string += str(data[i]) + " "
    print(string)

if __name__ == "__main__":
    # User inputs string w/ numbers
    user_input = input("Enter a space-separated string of numbers: ")

    # Call the function to process and print the result
    process_and_print(user_input)
