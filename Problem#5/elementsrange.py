def filter_and_print_range(input_list, min_val, max_val):
    output = []
    for i in range (len(input_list)):
        if (input_list[i] >= min_val and input_list[i] <= max_val):
            output.append(input_list[i])
    print(output)   
 
if __name__ == '__main__':
    # Get input for the list of integers
    user_input = input("Enter a space-separated string of numbers: ")
    filter_list = user_input.split()
   
    # Get input for the range (min and max values)
    user_input = input("Enter the min and max values separated by a space: ")
    tokens = user_input.split()
    min_val, max_val = tokens[0], tokens[1]
    

    # Call the function to filter and print the numbers in the given range
    filter_and_print_range(filter_list, min_val, max_val)
