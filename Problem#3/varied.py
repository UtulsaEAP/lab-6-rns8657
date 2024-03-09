def process_input(input_string):
   # Split into separate strings
    tokens = input_string.split()
    # Convert strings to floats
    data = []
    for i in range (len(tokens)):
        data.append(float(tokens[i]))
        

    # Get max and average
    max_value = max(data)
    average_value = sum(data) / len(data)
    return max_value, average_value

if __name__ == "__main__":
    # User inputs string w/ numbers
    user_input = input("Enter a space-separated string of numbers: ")

    # Call the function and get the results
    max_value, average_value = process_input(user_input)

    print(f'Max Value: {max_value:.2f}')
    print(f'Average Value: {average_value:.2f}')
