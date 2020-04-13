"""
Using helper functions
"""

# Context: solving all of the problems below in one function would be TOUGH and not produce
# the prettiest code. You should break the function up into smaller, helper functions.

# A prime number is a whole number greater than 1 whose only factors are 1 and
# itself. A factor is a whole number that can be divided evenly into another number.


num_list = [12, 15, 22, 13, 17, 11]

# TODO: Define a helper function called “isPrime” and pass it an argument of “num”.
# TODO: The function should determine whether or not the number is a prime number.
# TODO: Hint: you may want to iterate through numbers between 2 and the num argument
# TODO: minus one. With each of those numbers, you should check if there is a remainder
# TODO: using the modulo operator.

def isprime(num):
    p = "prime"
    for n in range(2,num):
        if (num % n == 0):
            p = "not prime"
            break
    return p

print(isprime(7))

 

# TODO: Define a helper function called "isEven" and pass it an argument of "num".
# TODO: If this function returns false, you should indicate in the "main" function
# TODO: that the number is odd.

def isEven(num):
    if (num % 2 == 0):
        return 'even'
    return 'odd'

print(isEven(7))



# TODO: Finally, define a function called "main" that accepts an argument "listy". listy will be
# TODO: a list of numbers. It should iterate through these numbers and call the above functions
# TODO: and produce an output for each, formatted as "Number ___ is (even or odd) and (prime or
# TODO: not prime)." Pass this function the "num_list" argument.

def main(listy):
   for num in listy:
       even = isEven(num) #isEven(num) is the return value of the isEven function
       prime = isprime(num) 
       print(f"{num} is {even} and {prime}")
       
main(num_list)
