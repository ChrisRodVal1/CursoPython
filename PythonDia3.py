#1. Create a program that takes a year as input and checks if it is a leap year or not/
def is_leap_year(year):
    if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
        return True
    else:
        return False

year = int(input("Enter a year: "))
if is_leap_year(year):
    print(f"The year {year} is a leap year.")
else:
    print(f"The year {year} is not a leap year.")



#2. Given a list of integers, find all the even numbers and store them in a new list/
def find_even_numbers(input_list):
    even_numbers = [num for num in input_list if num % 2 == 0]
    return even_numbers

input_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers_list = find_even_numbers(input_list)
print(f"The even numbers in the list are: {even_numbers_list}")



#3. Write a Python program to check if a given number is a prime number/
def is_prime(number):
    if number <= 1:
        return False
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False
    return True

num = int(input("Enter a number: "))
if is_prime(num):
    print(f"The number {num} is a prime number.")
else:
    print(f"The number {num} is not a prime number.")



#4. Create a program that generates the Fibonacci sequence up to a given number of terms/
def generate_fibonacci_sequence(n):
    sequence = []
    a, b = 0, 1
    for _ in range(n):
        sequence.append(a)
        a, b = b, a + b
    return sequence

num_of_terms = int(input("Enter the number of terms: "))
fib_sequence = generate_fibonacci_sequence(num_of_terms)
print(f"The Fibonacci sequence up to {num_of_terms} terms is: {fib_sequence}")



#5. Given a list of names, print all names starting with the letter 'A'.
def print_names_starting_with_a(names):
    for name in names:
        if name.startswith('A') or name.startswith('a'):
            print(name)

names_list = ['Alice', 'Bob', 'Anna', 'Alex', 'Daniel', 'Amy', 'Andrew']
print("Names starting with 'A':")
print_names_starting_with_a(names_list)



#6. Implement a program that prints the multiplication table of a given number/
def print_multiplication_table(number, limit):
    print(f"Multiplication table of {number}:")
    for i in range(1, limit + 1):
        print(f"{number} x {i} = {number * i}")

num = int(input("Enter a number: "))
table_limit = int(input("Enter the limit for the multiplication table: "))
print_multiplication_table(num, table_limit)



#7. Write a program that calculates the factorial of a given number/
def calculate_factorial(n):
    factorial = 1
    if n < 0:
        return "Factorial is not defined for negative numbers."
    elif n == 0:
        return 1
    else:
        for i in range(1, n + 1):
            factorial *= i
        return factorial

number = int(input("Enter a number: "))
result = calculate_factorial(number)
print(f"The factorial of {number} is: {result}")



#8. Create a loop that prints all prime numbers between 1 and 50/
def is_prime(number):
    if number <= 1:
        return False
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False
    return True

print("Prime numbers between 1 and 50:")
for num in range(2, 51):
    if is_prime(num):
        print(num)


#9. Given a list of words, count the number of words with more than five characters/
def count_words_with_more_than_five_characters(word_list):
    count = 0
    for word in word_list:
        if len(word) > 5:
            count += 1
    return count

word_list = ["apple", "banana", "cherry", "date", "elderberry", "fig", "grape"]
count = count_words_with_more_than_five_characters(word_list)
print(f"The number of words with more than five characters is: {count}")


#10. Calculate the sum of digits of a given number
def sum_of_digits(number):
    sum_digits = 0
    for digit in str(number):
        sum_digits += int(digit)
    return sum_digits

number = int(input("Enter a number: "))
result = sum_of_digits(number)
print(f"The sum of the digits of the number is: {result}")
