# For the following list of numbers:

numbers = [1, 6, 2, 2, 7, 1, 6, 13, 99, 7]

# 1. Print out a list of the even integers:


# 2. Print the difference between the largest and smallest value:


# 3. Print True if the list contains a 2 next to a 2 somewhere.


# 4. Print the sum of the numbers, 
#    BUT ignore any section of numbers starting with a 6 and extending to the next 7.
#    
#    So [11, 6, 4, 99, 7, 11] would have sum of 22


# 5. HARD! Print the sum of the numbers. 
#    Except the number 13 is very unlucky, so it does not count.
#    And numbers that come immediately after a 13 also do not count.
#    HINT - You will need to track the index throughout the loop.
#
#    So [5, 13, 2] would have sum of 5. 

# 1. Print out a list of the even integers:
for number in numbers:
    if number % 2 == 0:
        print(number)

# 2. Print the difference between the largest and smallest value:
numbers.sort()
difference = numbers[-1] - numbers[0]
print(numbers)
print(difference)

# 3. Print True if the list contains a 2 next to a 2 somewhere.
for number in numbers:
    if number == 2 and number is 2: 
        print(True)

# 4. Print the sum of the numbers, 
#    BUT ignore any section of numbers starting with a 6 and extending to the next 7.
sum_numbers = 0
for new_number in numbers:
    if new_number !=6:
        sum_numbers += new_number

print(sum_numbers)