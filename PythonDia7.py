#1. Given two dictionaries, merge them into a single dictionary
def merge_dictionaries(dict1, dict2):
    return {**dict1, **dict2}

dict1 = {'a': 1, 'b': 2}
dict2 = {'c': 3, 'd': 4}
merged_dict = merge_dictionaries(dict1, dict2)
print(f"The merged dictionary is: {merged_dict}")



#2. Write a program that finds the most frequent element in a list
from collections import Counter

def most_frequent_element(numbers):
    counter = Counter(numbers)
    most_common = counter.most_common(1)
    return most_common[0][0]

numbers = [1, 2, 3, 4, 2, 2, 4, 5, 3, 2, 2]
result = most_frequent_element(numbers)
print(f"The most frequent element in the list is: {result}")



#3. Implement a function that removes a key-value pair from a dictionary
def remove_key_value_pair(dictionary, key):
    if key in dictionary:
        del dictionary[key]

my_dict = {'a': 1, 'b': 2, 'c': 3}
print("Original dictionary:", my_dict)
remove_key_value_pair(my_dict, 'b')
print("Dictionary after removing key 'b':", my_dict)



#4. Create a program that checks if two sets have any elements in common
def check_common_elements(set1, set2):
    return len(set1.intersection(set2)) > 0

set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}
if check_common_elements(set1, set2):
    print("The two sets have common elements.")
else:
    print("The two sets do not have any common elements.")



#5. Given a list of dictionaries, find the dictionary with the highest value for a specific key
def find_dict_with_highest_value(dict_list, key):
    return max(dict_list, key=lambda x: x[key])

dict_list = [{'name': 'Alice', 'age': 30}, {'name': 'Bob', 'age': 25}, {'name': 'Charlie', 'age': 35}]
key_to_check = 'age'
result_dict = find_dict_with_highest_value(dict_list, key_to_check)
print(f"The dictionary with the highest value for key '{key_to_check}' is: {result_dict}")



#6. Write a Python program that counts the number of occurrences of each character in a given string using a dictionary
def count_character_occurrences(input_string):
    char_counts = {}
    for char in input_string:
        if char in char_counts:
            char_counts[char] += 1
        else:
            char_counts[char] = 1
    return char_counts

input_string = "hello world"
result = count_character_occurrences(input_string)
print("Character : Occurrences")
for key, value in result.items():
    print(f"{key} : {value}")



#7. Given two sets, find the union, intersection, and difference between them
def set_operations(set1, set2):
    union_set = set1.union(set2)
    intersection_set = set1.intersection(set2)
    difference_set1 = set1.difference(set2)
    difference_set2 = set2.difference(set1)
    return union_set, intersection_set, difference_set1, difference_set2

set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}
union, intersection, difference1, difference2 = set_operations(set1, set2)
print(f"The union of the two sets is: {union}")
print(f"The intersection of the two sets is: {intersection}")
print(f"The difference of set1 - set2 is: {difference1}")
print(f"The difference of set2 - set1 is: {difference2}")



#8. Create a function that takes a list of dictionaries and sorts them based on a specified key
def sort_list_of_dicts(dict_list, sort_key):
    return sorted(dict_list, key=lambda x: x[sort_key])

dict_list = [{'name': 'Alice', 'age': 30}, {'name': 'Bob', 'age': 25}, {'name': 'Charlie', 'age': 35}]
sort_key = 'age'
sorted_list = sort_list_of_dicts(dict_list, sort_key)
print("Sorted list of dictionaries:")
for dictionary in sorted_list:
    print(dictionary)



#9. Write a program that finds the average value of all the elements in a list of dictionaries
def average_value_of_elements(dict_list):
    count = 0
    total_sum = 0
    for dictionary in dict_list:
        for value in dictionary.values():
            total_sum += value
            count += 1
    return total_sum / count if count > 0 else 0

dict_list = [{'a': 10, 'b': 20, 'c': 30}, {'a': 15, 'b': 25, 'c': 35}, {'a': 20, 'b': 30, 'c': 40}]
average = average_value_of_elements(dict_list)
print(f"The average value of all elements in the list of dictionaries is: {average}")



#10. Implement a function that takes a list of strings and returns a set of unique characters present in all strings.
def find_common_characters(string_list):
    common_chars = set(string_list[0])
    for string in string_list[1:]:
        common_chars = common_chars.intersection(set(string))
    return common_chars

string_list = ['hello', 'world', 'python', 'java']
result = find_common_characters(string_list)
print(f"The set of common characters in all strings is: {result}")
