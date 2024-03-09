

def check_palindrome(user_input):
    reverse_input = ""
    for i in range (len(user_input) ):
        reverse_input += user_input[len(user_input) - 1 - i]

    if (user_input == reverse_input):
        print("palindrome: " + user_input)
    else:
        print("not a palindrome: " + user_input)

if __name__ == "__main__":
    user_input = input()
    check_palindrome(user_input)
