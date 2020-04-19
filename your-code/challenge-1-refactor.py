"""
This is a dumb calculator that can add and subtract integers from zero to five.
When you run the code, you are prompted to enter two numbers
and the operator sign (either in the form of English word or math signs).
The code will check your inputs to understand them, will perform the calculation
and give the result.

The code is refactored according to the following rules:
a) check your inputs until they meet the specified criteria (input error handling)
b) criteria for code simplicity and efficiency.
"""

# no libraries are imported
# input functions are coded first

# input function for numbers
# Input rules are --> an integer between zero and five (both inclusive)
# Error handling: keep asking for a number until it meets input criteria
def get_input_num(message):

    while True:
        try:
            userInput = int(input(message))
        except ValueError:
            print("Please enter an integer!")
        else:
            if ( (userInput > 5) | (userInput < 0) ):
                print("Please enter an integer 'n' such that: (0 <= 'n' <= 5)")
            else:
                return userInput

# input function for the operator (add or substract)
# Input rules are --> string case insensitive input must be 'plus' (or '+') or 'minus' (or '-')
# Error handling: keep asking your input until it meets criteria
def get_operator(message):

    choice = input(message)
    # check input
    while True:
        # first logic assestment: '+' or '-' signs (spaces omitted)
        plus1Bool  = (choice.strip(" ") == '+')
        minus1Bool = (choice.strip(" ") == '-')
        # second logic assestment: 'plus' or 'minus' strings (case insensitive/spaces omitted)
        plus2Bool  = (choice.lower().strip(" ") == 'plus')
        minus2Bool = (choice.lower().strip(" ") == 'minus')

        if plus1Bool or plus2Bool:
            return True
        elif minus1Bool or minus2Bool:
            return False
        else:
            choice = input("Please enter plus or minus! (+ or - also accepted)! ")

# main code: dumb calculator!
if __name__ == '__main__':

    print('Welcome to this calculator!')
    print('It can add or subtract integers (numbers) from zero to five (both inclusive)')

    a = get_input_num('Please choose your first number: ')
    operator = get_operator('What do you want to do? plus or minus: ')
    b = get_input_num('Please choose your second number: ')

    if operator:
        print(f"{a} + {b} = {a+b}")
    else:
        print(f"{a} - {b} = {a-b}")

    print("Thanks for using this calculator, goodbye :)")
