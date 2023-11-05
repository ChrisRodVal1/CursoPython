#1. Given a list of words, concatenate them into a single string separated by spaces'
def concatenate_words(words):
    return ' '.join(words)

words_list = ['Hello', 'world', 'this', 'is', 'a', 'test']
result = concatenate_words(words_list)
print(f"The concatenated string is: {result}")



#2. Create a function to reverse a given string' 
def reverse_string(input_string):
    return input_string[::-1]

string = input("Enter a string: ")
reversed_string = reverse_string(string)
print(f"The reversed string is: {reversed_string}")



#3. Write a program that takes a sentence as input and counts the number of words in it'
def count_words(sentence):
    words = sentence.split()
    return len(words)

input_sentence = input("Enter a sentence: ")
word_count = count_words(input_sentence)
print(f"The number of words in the sentence is: {word_count}")



#4. Implement a function that checks if a given string is a pangram (contains all letters of the alphabet)'
import string

def is_pangram(s):
    alphabet = set(string.ascii_lowercase)
    return set(s.lower()) >= alphabet

input_string = input("Enter a string: ")
if is_pangram(input_string):
    print("The string is a pangram.")
else:
    print("The string is not a pangram.")



#5. Given a string, write a function to remove all vowels from it and return the modified string'
def remove_vowels(input_string):
    vowels = "aeiouAEIOU"
    return ''.join(char for char in input_string if char not in vowels)

string = input("Enter a string: ")
modified_string = remove_vowels(string)
print(f"The modified string after removing vowels is: {modified_string}")



#6. Write a Python program to find the length of the longest word in a sentence'
def longest_word_length(sentence):
    words = sentence.split()
    longest_length = 0
    for word in words:
        longest_length = max(longest_length, len(word))
    return longest_length

input_sentence = input("Enter a sentence: ")
length = longest_word_length(input_sentence)
print(f"The length of the longest word in the sentence is: {length}")



#7. Create a function that takes a sentence as input and returns the sentence in reverse order'
def reverse_sentence_order(sentence):
    words = sentence.split()
    reversed_sentence = ' '.join(reversed(words))
    return reversed_sentence

input_sentence = input("Enter a sentence: ")
reversed_sentence = reverse_sentence_order(input_sentence)
print(f"The sentence in reverse order is: {reversed_sentence}")


#8. Given a list of names, count the number of names that start with a vowel'
def count_names_starting_with_vowel(names):
    vowels = 'aeiouAEIOU'
    count = 0
    for name in names:
        if name[0] in vowels:
            count += 1
    return count

names_list = ['Alice', 'Bob', 'Eva', 'Daniel', 'Olivia', 'Ian', 'Ursula']
result = count_names_starting_with_vowel(names_list)
print(f"The number of names starting with a vowel is: {result}")



#9. Write a function to remove all duplicate characters from a given string'
def remove_duplicates(input_string):
    return ''.join(sorted(set(input_string), key=input_string.index))

string = input("Enter a string: ")
result = remove_duplicates(string)
print(f"The string after removing duplicates is: {result}")



#10. Implement a program that takes a sentence and a word as input and checks if the word is present in the sentence.
def check_word_in_sentence(sentence, word):
    words = sentence.split()
    return word in words

sentence = input("Enter a sentence: ")
search_word = input("Enter a word to search: ")
if check_word_in_sentence(sentence, search_word):
    print(f"The word '{search_word}' is present in the sentence.")
else:
    print(f"The word '{search_word}' is not present in the sentence.")
