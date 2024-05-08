def process_and_print(input_string):
    
  all_num = input_string.split()
   
  int_num = list(map(int, all_num))

  negative_num = list(filter(lambda n: n < 0,int_num))
    
  negative_num.sort(reverse=True)
    
  for value in negative_num:
    print(value, end=' ')         
    

if __name__ == "__main__":
    
    user_input = input("Enter a space-separated string of numbers: ")

   
    process_and_print(user_input)

