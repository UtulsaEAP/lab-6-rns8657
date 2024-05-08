def filter_and_print_range(integer_list, min_val, max_val):
    for _ in integer_list:
        if min_val <= _ <= max_val:
            print(_, end=',')

 
if __name__ == '__main__':
    # Get input for the list of integers
    user_input = input("Enter a space-separated string of numbers: ")
    integer_list = list(map(int, user_input.split()))
   
    # Get input for the range (min and max values)
    user_input = input("Enter the min and max values separated by a space: ")
    min_val, max_val = list(map(int, (user_input.split())))
    
    filter_and_print_range(integer_list, min_val, max_val)

