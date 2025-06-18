# (Question 1).Write a program in Python to perform the following operation:
# If a number is divisible by 3 it should print “SKILLBREW”as a string
# If a number is divisible by 5 it should print “BRUDITE” as a string
# If a number is divisible by both 3 and 5 it should print “BRUDITE - NIRVANA” as a string.
# Function to check divisibility and print result

def check_number(num):
    if num % 3 == 0 and num % 5 == 0:
        print("BRUDITE - NIRVANA")
    elif num % 3 == 0:
        print("SKILLBREW")
    elif num % 5 == 0:
        print("BRUDITE")
    else:
        print("Number is not divisible by 3 or 5")

number = int(input("Enter a number: "))
check_number(number)

#(Question 2).2. Write a program that accepts a string as input from the user and calculates the number of digits and letters.
# Input: Hello123
# Output: Alphabets: 5 & Number : 3

user_input = input("Enter a string: ")

letters = 0
digits = 0

for char in user_input:
    if char.isalpha():
        letters += 1
    elif char.isdigit():
        digits += 1

print(f"Alphabets: {letters} & Number: {digits}")

# (Question 3). Write a Python program to input marks for five subjects Physics, Chemistry, Biology, Mathematics, and Computer.
#  Calculate the percentage and grade
#  according to the following:
#  Percentage >= 90% : Grade A
#  Percentage >= 80% : Grade B
#  Percentage >= 70% : Grade C
#  Percentage >= 60% : Grade D
#  Percentage >= 40% : Grade E
#  Percentage < 40% : Grade F


physics = float(input("Enter marks for Physics: "))
chemistry = float(input("Enter marks for Chemistry: "))
biology = float(input("Enter marks for Biology: "))
mathematics = float(input("Enter marks for Mathematics: "))
computer = float(input("Enter marks for Computer: "))

total_marks = physics + chemistry + biology + mathematics + computer
percentage = (total_marks / 500) * 100

if percentage >= 90:
    grade = "A"
elif percentage >= 80:
    grade = "B"
elif percentage >= 70:
    grade = "C"
elif percentage >= 60:
    grade = "D"
elif percentage >= 40:
    grade = "E"
else:
    grade = "F"

print(f"\nTotal Marks: {total_marks}/500")
print(f"Percentage: {percentage:.2f}%")
print(f"Grade: {grade}")

# (Question 4). Write a Python program to find the sum of all odd  numbers between two given numbers. 
# Start = 1, stop = 10
# Sum of odd numbers: 25


start = int(input("Enter the starting number: "))
stop = int(input("Enter the stopping number: "))

odd_sum = 0

for num in range(start, stop + 1):
    if num % 2 != 0:
        odd_sum += num

print(f"Sum of odd numbers: {odd_sum}")

# (Question 5). Write a Python program to find the factorial of a number using a for loop


num = int(input("Enter a number: "))

factorial = 1

if num < 0:
    print("Factorial does not exist for negative numbers.")
elif num == 0:
    print("The factorial of 0 is 1.")
else:
    for i in range(1, num + 1):
        factorial *= i
    print(f"The factorial of {num} is {factorial}.")

# (Question 6). Write a Python program to check if a given number is a perfect number. 
# A Perfect number is a positive integer that is equal to the sum of its proper divisors. For instance, 6 has divisors 1, 2,
# and 3, and 1 + 2 + 3 = 6, so 6 is a perfect number.
#   Input: 5 
#   Output: No

num = int(input("Enter a number: "))

sum_of_divisors = 0

for i in range(1, num):
    if num % i == 0:
        sum_of_divisors += i

if sum_of_divisors == num:
    print("Yes, it's a Perfect Number")
else:
    print("No, it's not a Perfect Number")

# (Question 7). Write a Python program to check if a string is an anagram of another string.
#  string1 = "listen", string2 = "silent"
#  Output: True

str1 = input("Enter first string: ")
str2 = input("Enter second string: ")

if sorted(str1) == sorted(str2):
    print("True")
else:
    print("False")


# (Question 9). Write a Python program to count the frequency of each element in a list.
#   Input_list = [1, 2, 3, 2, 4, 1, 2, 4, 5]
#   Frequency count: {1: 2, 2: 3, 3: 1, 4: 2, 5: 1}


input_list = [1, 2, 3, 2, 4, 1, 2, 4, 5]
frequency = {}

for item in input_list:
    if item in frequency:
        frequency[item] += 1
    else:
        frequency[item] = 1

print("Frequency count:", frequency)

# (Question 10). Write a Python program to reverse the order of words in a given sentence.
#  Input_sentence = “Hello, World! Welcome to Python programming.”
#  Output after reverse = “programming. Python to Welcome World! Hello,”

input_sentence = "Hello, World! Welcome to Python programming."

reversed_words = input_sentence.split()[::-1]

reversed_sentence = ' '.join(reversed_words)

print("Output after reverse:", reversed_sentence)

# (Question 11). Write a Python program to calculate the sum of digits of a given number until the sum becomes a single-digit number.
#      Sample Input: num = 987
#      Sample Output: Sum_of_digits = 24,
#      Again compute the sum of digits so that it can be reduced
#  to
#      on single digit.
#      Final Output: 6

def sum_of_digits(num):
    while num >= 10:
        total = 0
        while num > 0:
            total += num % 10
            num //= 10
        print(f"Intermediate sum: {total}")
        num = total
    return num

num = int(input("Enter a number: "))

final_sum = sum_of_digits(num)
print("Final Output:", final_sum)

# (Question 12). Write a Python program to reverse a number using
#  a while loop.
#      Sample Input: num = 12345
#      Sample Output: revnum = 54321

num = int(input("Enter a number: "))

revnum = 0

while num > 0:
    digit = num % 10       
    revnum = revnum * 10 + digit  
    num = num // 10          

print("Reversed number:", revnum)
