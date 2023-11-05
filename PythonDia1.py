#1. Write a Python program to calculate the area of a rectangle given its length and width
def calculate_rectangle_area(length, width):
    area = length * width
    return area
length = float(input("Enter the length of the rectangle: "))
width = float(input("Enter the width of the rectangle: "))

area = calculate_rectangle_area(length, width)
print(f"The area of the rectangle is: {area}")


#2. Create a program that takes a user's name and age as input and prints a greeting message
def greet_user():
    name = input("Please enter your name: ")
    age = input("Please enter your age: ")

    print(f"Hello {name}! You are {age} years old. Welcome!")
    
greet_user()


#3. Write a program to check if a number is even or odd
def check_even_odd(number):
    if number % 2 == 0:
        print(f"The number {number} is even.")
    else:
        print(f"The number {number} is odd.")

number = int(input("Enter a number: "))
check_even_odd(number)


#4. Given a list of numbers, find the maximum and minimum values
def find_max_min(numbers):
    max_value = max(numbers)
    min_value = min(numbers)
    return max_value, min_value

numbers = [3, 7, 1, 9, 4, 5]
max_value, min_value = find_max_min(numbers)
print(f"The maximum value in the list is: {max_value}")
print(f"The minimum value in the list is: {min_value}")


#5. Create a Python function to check if a given string is a palindrome
def is_palindrome(s):
    s = s.lower() 
    reversed_s = s[::-1] 

    if s == reversed_s:
        return True
    else:
        return False

string = input("Enter a string: ")
if is_palindrome(string):
    print(f"The string '{string}' is a palindrome.")
else:
    print(f"The string '{string}' is not a palindrome.")



#6. Calculate the compound interest for a given principal amount, interest rate, and time period
def calculate_compound_interest(principal, rate, time, compounds_per_year):
    amount = principal * (1 + rate/compounds_per_year) ** (compounds_per_year*time)
    return amount

principal = float(input("Enter the principal amount: "))
rate = float(input("Enter the annual interest rate (in decimal form): "))
time = float(input("Enter the time period in years: "))
compounds_per_year = int(input("Enter the number of times the interest is compounded per year: "))

result = calculate_compound_interest(principal, rate, time, compounds_per_year)
print(f"The compound interest after {time} years will be: {result}")


#7. Write a program that converts a given number of days into years, weeks, and days
def convert_days(number_of_days):
    years = number_of_days // 365
    weeks = (number_of_days % 365) // 7
    days = number_of_days - (years * 365) - (weeks * 7)
    return years, weeks, days

number_of_days = int(input("Enter the number of days: "))
years, weeks, days = convert_days(number_of_days)
print(f"{number_of_days} days is equal to {years} years, {weeks} weeks, and {days} days.")

#8. Given a list of integers, find the sum of all positive numbers
def sum_of_positive_numbers(numbers):
    sum_positive = 0
    for num in numbers:
        if num > 0:
            sum_positive += num
    return sum_positive

integer_list = [3, -5, 2, 0, 8, -1, 4, -6]
positive_sum = sum_of_positive_numbers(integer_list)
print(f"The sum of all positive numbers in the list is: {positive_sum}")


#9. Create a program that takes a sentence as input and counts the number of words in it
def count_words(sentence):
    words = sentence.split()
    return len(words)

sentence = input("Enter a sentence: ")
word_count = count_words(sentence)
print(f"The number of words in the sentence is: {word_count}")


#10. Implement a program that swaps the values of two variables
def swap_variables(a, b):
    temp = a
    a = b
    b = temp
    return a, b

var1 = input("Enter the first variable: ")
var2 = input("Enter the second variable: ")

print(f"Before swapping: var1 = {var1}, var2 = {var2}")
var1, var2 = swap_variables(var1, var2)
print(f"After swapping: var1 = {var1}, var2 = {var2}")
