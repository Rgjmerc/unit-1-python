"""
Exercise 1:
Write a program to print numbers from 1 to 10 using a for loop.
"""

for x in range (1,11):
    #add one since exclusive
    print(x)

"""
Exercise 2:
Write a program to count by 10s from 900 to 1000
"""

for y in range (900,1001,10):
    # multiples of 10 due to the 3rd placement
    print(y)

"""
Exercise 3:
Write a program that counts form 1-100 by 9
"""

for z in range (1, 101, 9):
    print(z)

"""
Exercise 4:
Write a program to calculate the sum of all numbers from 1 to 10 using a for loop.
"""

numbers = 0
for n in range (1, 11):
    numbers += n
print(numbers)

"""
Excercise 5:
Uncomment the following code and run it. Then answer the following:
- What is the ouput of the code?

- Explain the iterative process that this code executes to get that output
"""

rows = 5
for i in range(rows):
     for j in range(i + 1):
         print('*', end=' ')
     print()
#the code adds one new * per row for 5 rows
#the reason the code outputs this is because of the range and the i+1 causing more to be printed each row