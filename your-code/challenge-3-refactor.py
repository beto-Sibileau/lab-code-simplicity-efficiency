"""
You are presented with an integer number larger or equal than 5.
Your goal is to identify the longest side possible in a right triangle
whose sides are not longer than the number you are given.

For example, if you are given the number 14, there are 3 possibilities
to compose right triangles:

1. [3, 4, 5]
2. [6, 8, 10]
3. [5, 12, 13]

The following function shows an efficient way to solve the problem
trying the fewest possible number of cpu iterations
"""

# input integer number function with error handling
def input_integer(message):
    while True:
        try:
            number = int(input(message))
        except ValueError:
            print("Please enter an integer!")
        else:
            return number

# core function optimized
def my_function_eff(x):
    # Interested in the maximum? Ranges ordered descending
    # Starting point of ranges modified for efficiency
    range5inv = range(x,4,-1)
    range4inv = range(x-1,3,-1)
    range3inv = range(x-2,2,-1)
    
    # I avoid list comprehension to make code more readable
    for x in range5inv:
        range4dyn = filter(lambda y:y < x, range4inv)
        # Range below adapted for efficiency
        for y in range4dyn:
            range3dyn = filter(lambda z:z < y, range3inv)
            # Range below adapted for efficiency
            for z in range3dyn:
                if x**2==y**2+z**2:
                    return x

# main code: call functions (input and core), print result
if __name__ == '__main__':

    x = input_integer("What is the maximal length of the triangle side? Enter an integer: ")
    print(f"The longest side possible is {my_function_eff(x)}")
