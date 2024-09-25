"""
Exercise 1:
Write a program to print each character of a given string using a for loop.
"""

body="head"
for x in body:
    print(x)
    #prints each individual letter 


"""
Exercise 2:
Write a program to calculate the sum of elements in a list using a for loop.
"""

numlist=[2,7,8,3,4,9]
sum = 0
for num in numlist:
     sum += num
     #adds all values of the list
print(sum)

"""
Exercise 3:
Write a program to print the length of each word in a sentence using a for loop and a list.
"""

digbar = "Four Big Guys"
words = digbar.split(" ")
#splits all words
letters = 0
for z in  words:
     letters =  len(z)
     #counts letters for the current word
     print(letters)
     #loops and prints until all words letter counts are complete
"""
Excercise 4:
Write a program that creates a dictionary (atleast 4 key:value pairs) and then
iterates through a dictionary and prints the result

In a comment, answer the following, what do you notice about the output of your code?
Is it what you expected?
"""

fruits = {
     "apples": 6,
     "bananas": 7,
     "cherries": 5
}
#the dictionary
for f in fruits:
     print(fruits[f])
#prints values of dictionaries