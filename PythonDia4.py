#1. Given a list of numbers, create a function to find the sum of all positive numbers-
def sum_of_positive_numbers(numbers):
    sum_positive = 0
    for num in numbers:
        if num > 0:
            sum_positive += num
    return sum_positive

numbers = [1, -2, 3, -4, 5, -6, 7, -8, 9]
result = sum_of_positive_numbers(numbers)
print(f"The sum of all positive numbers in the list is: {result}")



#2. Write a Python function to check if a given string is a palindrome-
def is_palindrome(s):
    s = s.lower() 
    return s == s[::-1]

input_string = input("Enter a string: ")
if is_palindrome(input_string):
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")



#3. Implement a function that returns the factorial of a given number using recursion-
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

number = int(input("Enter a number: "))
result = factorial(number)
print(f"The factorial of {number} is: {result}")



#4. Create a function to find the square of each element in a given list-
def square_elements(numbers):
    return [x ** 2 for x in numbers]

input_list = [1, 2, 3, 4, 5]
result = square_elements(input_list)
print(f"The squares of the elements in the list are: {result}")



#5. Write a function to check if a number is even or odd and return "Even" or "Odd" accordingly.
def even_or_odd(number):
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"

num = int(input("Enter a number: "))
result = even_or_odd(num)
print(f"The number is {result}.")



#6. Calculate the area of a triangle given its base and height using a function-
def calculate_triangle_area(base, height):
    return 0.5 * base * height

base = float(input("Enter the base of the triangle: "))
height = float(input("Enter the height of the triangle: "))
area = calculate_triangle_area(base, height)
print(f"The area of the triangle is: {area}")



#7. Create a function that takes a list of strings and returns the list sorted alphabetically-
def sort_strings(strings):
    return sorted(strings)

input_list = ['banana', 'apple', 'cherry', 'date']
sorted_list = sort_strings(input_list)
print(f"The sorted list of strings is: {sorted_list}")



#8. Write a function that takes two lists and returns their intersection (common elements)-
def find_list_intersection(list1, list2):
    return list(set(list1) & set(list2))

list1 = [1, 2, 3, 4, 5]
list2 = [3, 4, 5, 6, 7]
intersection = find_list_intersection(list1, list2)
print(f"The intersection of the two lists is: {intersection}")



#9. Implement a function to check if a given year is a leap year or not-
def is_leap_year(year):
    if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
        return True
    else:
        return False

year = int(input("Enter a year: "))
if is_leap_year(year):
    print(f"{year} is a leap year.")
else:
    print(f"{year} is not a leap year.")



#10. Create a function that takes a number as input and prints its multiplication table.
def print_multiplication_table(number):
    for i in range(1, 11):
        print(f"{number} x {i} = {number * i}")
        
num = int(input("Enter a number: "))
print_multiplication_table(num)
