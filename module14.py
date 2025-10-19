# Question 7: Value returning function named half 
# The following statement calls a function named half, which returns a value that is half that of the argument (Assume the number variable references a float value.) Write code for the function.

# result = half(number)
# Question 7

def half(num):
    return (num / 2)

input_number = int(input())

result = half(input_number);

print(f"{result}")

# Question 6

# Question 6: Using Python's random number function
# Write a statement that generates a random number in the range of 1 through 100 and assigns it to a variable named rand.
import random;

def ran_number():
    rand = random.randint(1, 101)
    print(f"{rand}")

ran_number()