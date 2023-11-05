#1. Given two lists of numbers, concatenate them into a single list
def concatenate_lists(list1, list2):
    return list1 + list2

list1 = [1, 2, 3]
list2 = [4, 5, 6]
concatenated_list = concatenate_lists(list1, list2)
print(f"The concatenated list is: {concatenated_list}")



#2. Write a program that finds the largest and smallest elements in a list
def find_max_min_elements(numbers):
    largest = max(numbers)
    smallest = min(numbers)
    return largest, smallest

numbers = [12, 45, 23, 67, 3, 18, 9, 31, 8]
largest, smallest = find_max_min_elements(numbers)
print(f"The largest element in the list is: {largest}")
print(f"The smallest element in the list is: {smallest}")



#3. Implement a function that takes a list of numbers and returns a new list with the squared values
def square_values(numbers):
    return [num ** 2 for num in numbers]

numbers = [1, 2, 3, 4, 5]
squared_values = square_values(numbers)
print(f"The squared values of the list are: {squared_values}")



#4. Create a program that finds the common elements between two lists and stores them in a new list5
def find_common_elements(list1, list2):
    common_elements = list(set(list1) & set(list2))
    return common_elements

list1 = [1, 2, 3, 4, 5]
list2 = [3, 4, 5, 6, 7]
common_elements = find_common_elements(list1, list2)
print(f"The common elements between the two lists are: {common_elements}")



#5. Given a list of words, find the word with the maximumlength and its length
def find_longest_word(words):
    longest_word = max(words, key=len)
    return longest_word, len(longest_word)

words = ['apple', 'banana', 'grapefruit', 'cherry', 'peach']
longest_word, length = find_longest_word(words)
print(f"The longest word in the list is '{longest_word}' with a length of {length} characters.")



#6. Write a Python program to count the occurrences of each element in a given list
def count_occurrences(numbers):
    counts = {}
    for num in numbers:
        if num in counts:
            counts[num] += 1
        else:
            counts[num] = 1
    return counts

numbers = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
occurrences = count_occurrences(numbers)
print("Element : Occurrences")
for key, value in occurrences.items():
    print(f"{key} : {value}")



#7. Given a list of names, remove all duplicate names and print the unique names
def remove_duplicates_from_list(names):
    unique_names = list(set(names))
    return unique_names

names = ['Alice', 'Bob', 'Alice', 'Charlie', 'Bob']
unique_names = remove_duplicates_from_list(names)
print("The unique names in the list are:")
for name in unique_names:
    print(name)



#8. Create a function that takes a list of strings and returns the list sorted by the length of the strings
def sort_by_length(strings):
    return sorted(strings, key=len)

strings = ['banana', 'apple', 'cherry', 'date']
sorted_strings = sort_by_length(strings)
print("The list sorted by length of strings is:")
for string in sorted_strings:
    print(string)



#9. Write a program that checks if a given list is sorted in ascending order
def is_sorted_ascending(numbers):
    return all(numbers[i] <= numbers[i + 1] for i in range(len(numbers) - 1))

numbers1 = [1, 2, 3, 4, 5]
numbers2 = [1, 3, 2, 4, 5]
if is_sorted_ascending(numbers1):
    print("The list is sorted in ascending order.")
else:
    print("The list is not sorted in ascending order.")

if is_sorted_ascending(numbers2):
    print("The list is sorted in ascending order.")
else:
    print("The list is not sorted in ascending order.")



#10. Implement a function that takes two lists and returns their union (all unique elements from both lists).
def find_union(list1, list2):
    return list(set(list1) | set(list2))

list1 = [1, 2, 3, 4, 5]
list2 = [3, 4, 5, 6, 7]
union_list = find_union(list1, list2)
print(f"The union of the two lists is: {union_list}")
