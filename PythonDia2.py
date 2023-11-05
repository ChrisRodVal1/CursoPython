#1. Given a list of numbers, find the sum and average'
def calculate_sum_and_average(numbers):
    total_sum = sum(numbers)
    average = total_sum / len(numbers)
    return total_sum, average

number_list = [2, 4, 6, 8, 10]
total_sum, average = calculate_sum_and_average(number_list)
print(f"The sum of the numbers is: {total_sum}")
print(f"The average of the numbers is: {average}")


#2. Create a program that takes a temperature in Celsius and converts it to Kelvin'
def celsius_to_kelvin(celsius):
    kelvin = celsius + 273.15
    return kelvin

celsius = float(input("Enter the temperature in Celsius: "))
kelvin = celsius_to_kelvin(celsius)
print(f"The temperature {celsius} Celsius is equal to {kelvin} Kelvin.")


#3. Implement a program that checks if a given string is a palindrome'
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
    
    
#4. Create a function to reverse a given string'
def reverse_string(s):
    return s[::-1]

string = input("Enter a string: ")
reversed_string = reverse_string(string)
print(f"The reversed string is: {reversed_string}")


#5. Given a list of names, concatenate them into a single string separated by spaces'
def concatenate_names(names):
    concatenated_string = ' '.join(names)
    return concatenated_string

names_list = ["John", "Doe", "Jane", "Smith", "Tom"]
result_string = concatenate_names(names_list)
print(f"The concatenated string is: {result_string}")


#6. Write a Python program to check if a given string is a pangram (contains all letters of the alphabet)'
import string

def is_pangram(sentence):
    alphabet_set = set(string.ascii_lowercase)
    sentence_set = set(sentence.lower())
    return alphabet_set.issubset(sentence_set)

input_string = input("Enter a sentence: ")
if is_pangram(input_string):
    print("The sentence is a pangram.")
else:
    print("The sentence is not a pangram.")


#7. Calculate the area and circumference of a circle given its radius'
import math

def calculate_circle_properties(radius):
    area = math.pi * radius ** 2
    circumference = 2 * math.pi * radius
    return area, circumference

radius = float(input("Enter the radius of the circle: "))
area, circumference = calculate_circle_properties(radius)
print(f"The area of the circle is: {area}")
print(f"The circumference of the circle is: {circumference}")


#8. Implement a program that converts a given number of minutes into hours and minutes'
def convert_minutes_to_hours_and_minutes(minutes):
    hours = minutes // 60
    remaining_minutes = minutes % 60
    return hours, remaining_minutes

total_minutes = int(input("Enter the total number of minutes: "))
hours, minutes = convert_minutes_to_hours_and_minutes(total_minutes)
print(f"{total_minutes} minutes is equal to {hours} hours and {minutes} minutes.")


#9. Create a function to count the number of vowels in a given string'
def count_vowels(s):
    vowels = "aeiouAEIOU"
    count = 0
    for char in s:
        if char in vowels:
            count += 1
    return count

input_string = input("Enter a string: ")
num_vowels = count_vowels(input_string)
print(f"The number of vowels in the string is: {num_vowels}")


#10. Write a program to check if a number is prime.
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
