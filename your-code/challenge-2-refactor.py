
"""
The code below generates a given number of random strings that consists of numbers and 
lower case English letters. You can also define the range of the variable lengths of
the strings being generated.

The code has been refactored using simplifications and and efficiency considerations.
"""

# imported libraries
import string
import random

# input number for batch of strings length
def get_batch_length():
    while True:
        try:
            number = int(input("How many random strings to generate? "))
        except ValueError:
            print("Please enter an integer!")
        else:
            return number
            
# input function for min and max string lengths
# max must be greater or equal to min
def get_stringLen_bounds():
    while True:
        try:
            userMin = int(input("Enter minimum string length: "))
            break
        except ValueError:
            print("Please enter an integer!")

    while True:
        try:
            userMax = int(input("Enter maximum string length: "))
        except ValueError:
            print("Please enter an integer, try again!")
        else:
            if userMax < userMin:
                print("Maximum lower than minimum, please enter again!")
            else:
                break
    return (userMin,userMax)

# generate a random string of a specified length
# string contains lowercase letters and/or numbers
stringConcat = string.ascii_lowercase + string.digits
def generate_rand_string(length = 12, strings = stringConcat):
    counter = 0
    strGene = ''
    while counter < length:
        strGene += random.choice(strings)
        counter += 1
    return strGene
    
# collects a batch of random strings in a list of variable length 'batchLen'
# strings length is random as well, between lower and upper bounds (lBound, uBound)
def generate_batch_string(batchLen = 1, lBound = 8, uBound = 12):
    if uBound >= lBound:
        # generate a list (length=batchLen) with random numbers between lBound and uBound
        randStringLen = [random.randrange(lBound,uBound+1) for i in range(batchLen)]
        # populate the batch of random strings calling generate_rand_string
        batch = [generate_rand_string(length) for length in randStringLen]
        return batch
    else:
        print("Batch of strings not returned.\nBounds must be 'lBound <= uBound' for strings length.")

# main code: call functions (input and generate_batch_string), print result
if __name__ == '__main__':

    (lowerBound,upperBound) = get_stringLen_bounds()
    batchLength             = get_batch_length()
    print(generate_batch_string(batchLength,lowerBound,upperBound))
