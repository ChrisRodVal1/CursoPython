numbers = [5, 2, 8, 1, 9, 3, 4, 7, 6]
list1 = [1, 2, 3, 4, 5]
list2 = [3, 4, 5, 6, 7]
words = ['apple', 'banana', 'grapefruit', 'cherry', 'peach']
names = ['Alice', 'Bob', 'Alice', 'Charlie', 'Bob']
strings = ['banana', 'apple', 'cherry', 'date']

#1. Write a program that finds the largest and smallest elements in a list
def find_largest_and_smallest_elements(numbers):
    return max(numbers), min(numbers)

largest, smallest = find_largest_and_smallest_elements(numbers)
print(f"Largest element: {largest}, Smallest element: {smallest}")


#2. Implement a function that takes a list of numbers and returns a new list with the squared values
def find_squared_values(numbers):
    return [num ** 2 for num in numbers]

squared_values = find_squared_values(numbers)
print(f"Squared values: {squared_values}")


#3. Create a program that finds the common elements between two lists and stores them in a new list
def find_common_elements(list1, list2):
    return list(set(list1) & set(list2))

common_elements = find_common_elements(list1, list2)
print(f"Common elements: {common_elements}")


#4. Given a list of words, find the word with the maximum length and its length
def find_longest_word(words):
    longest_word = max(words, key=len)
    return longest_word, len(longest_word)

longest_word, length = find_longest_word(words)
print(f"The longest word is '{longest_word}' with a length of {length} characters.")


#5.6. Write a Python program to count the occurrences of each element in a given list
def count_element_occurrences(numbers):
    counts = {}
    for num in numbers:
        if num in counts:
            counts[num] += 1
        else:
            counts[num] = 1
    return counts

occurrences = count_element_occurrences(numbers)
print("Element : Occurrences")
for key, value in occurrences.items():
    print(f"{key} : {value}")
    
    
#7. Given a list of names, remove all duplicate names and print the unique names
def remove_duplicates_from_list(names):
    unique_names = list(set(names))
    return unique_names

unique_names = remove_duplicates_from_list(names)
print("Unique names:", unique_names)


#8. Create a function that takes a list of strings and returns the list sorted by the length of the strings
def sort_by_length(strings):
    return sorted(strings, key=len)

sorted_strings = sort_by_length(strings)
print("Sorted strings:", sorted_strings)


#9. Write a program that checks if a given list is sorted in ascending order
def is_sorted_ascending(numbers):
    return all(numbers[i] <= numbers[i + 1] for i in range(len(numbers) - 1))

if is_sorted_ascending(numbers):
    print("The list is sorted in ascending order.")
else:
    print("The list is not sorted in ascending order.")

#10. Implement a function that takes two lists and returns their union (all unique elements from both lists).
def find_union(list1, list2):
    return list(set(list1) | set(list2))

union_list = find_union(list1, list2)
print(f"The union of the two lists is: {union_list}")
