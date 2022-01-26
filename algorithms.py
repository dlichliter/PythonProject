# Print the numbers from 1 to 100, replacing multiples of 3 with fizz, 5 with buzz, and 3 and 5 with fizzbuzz
def fizz_buzz():
    for i in range(1, 101):
        if i % 3 == 0 and i % 5 == 0:
            print('fizzbuzz')
        elif i % 3 == 0:
            print('fizz')
        elif i % 5 == 0:
            print('buzz')
        else:
            print(i)


# fizz_buzz()


# Check though a list of numbers sequentially to see if a number is in the list
# returning true if it is found and false else wise
def simple_search(number_list, n):
    found = False

    for nb in number_list:
        if nb == n:
            found = True
            break
    return found


# numbers = range(0, 100)
# s1 = simple_search(numbers, 2)
# print(s1)
# s2 = simple_search(numbers, 202)
# print(s2)


# Check if a word is a palindrome
def palindrome(word):
    # Handle capitalization differences between start/end of word
    word = word.lower()
    # Slice the word in reverse, then return true if matches or false otherwise
    return word[::-1] == word

#
# print(palindrome("String"))
# print(palindrome("Racecar"))


# Check if two words are anagrams of each other, returning true if they are or false otherwise
def anagram(word1, word2):
    word1 = word1.lower()
    word2 = word2.lower()
    return sorted(word1) == sorted(word2)


# print(anagram("Undertale", "Deltarune"))
# print(anagram("Too", "Two"))


# Count the number of times a letter is used in a string, returning a dictionary
def count_characters(string):
    character_count = {}
    for char in string:
        if char in character_count:
            character_count[char] += 1
        else:
            character_count[char] = 1
    return character_count


# print(count_characters("Scooter"))


# Recursively print the song X bottles of beer where X is a positive integer
def bottles_of_beer(bottles):
    if bottles < 1:
        print("""No more bottles of beer on the wall.
        No more bottles of beer.""")
        return
    elif bottles == 1:
        print("""1 bottle of beer on the wall.
        1 bottle of beer.
        Take it down, pass it around,
        No bottles of beer on the wall.""")
    else:
        print("""{} bottles of beer on the wall.
        {} bottles of beer.
        Take one down, pass it around,
        {} bottles of beer on the wall.""".format(bottles, bottles, bottles - 1))
    bottles -= 1
    bottles_of_beer(bottles)


# bottles_of_beer(99)
