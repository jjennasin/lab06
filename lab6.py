#  Jenna Sin

encoded = "0"  # created a global variable

def encode(string):  # adds 3 to each digit
    global encoded
    encoded = ""  # empty string
    for i in string:  # iterate through the string
        i = int(i)
        if i < 7:  # if the number won't go over 10
            i += 3  # add 3
        elif i >= 7:  # if the number exceeds 10
            i -= 7  # gets the second digit of the digit plus 3
        encoded += str(i)
    return encoded


# John Kellen decode function
def decode():
    global encoded

    result = ''

    if encoded == None:
        return 'Error'

    for i in encoded:

        i = int(i)
        if i <= 2:
            i = i + 7
        else:
            i -= 3

        i = str(i)

        result += i

    return result


def print_menu():
    print("Menu")
    print("-------------")
    print("1. Encode\n2. Decode\n3. Quit")



if __name__ == "__main__":
    choice = 0
    while True:
        print_menu()
        choice = int(input("Please enter an option: "))
        if choice == 3:
            break
        if choice == 1:
            string = input("Please enter your password to encode: ")
            encode(string)
            print("Your password has been encoded and stored!")
        if choice == 2:
            print(f"The encoded password is {encoded}, and the original password is {decode()}.")
