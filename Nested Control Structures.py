'''
Programmer: Andrew Gowan
Date: 10.15.19
Program: Double For Loop

This Program will nest a For Loop inside of another
For Loop
'''

for i in range(3):
    print("Outer For Loop: " + str(i))
    for l in range(2):
        print("     Inner For Loop: " + str(l))

print("\n**********\n")


'''
Programmer: Andrew Gowan
Date: 10.22.19
Program: Average Test Scores

This Program asks for the test scores for multiple people
and reports the average test score for each portion
'''

num_people = int(input("How many people are taking the test?: "))
test_per_person = int(input("How many tests are going to be averaged?: "))

for i in range(num_people):
    name = input("Enter name: ")
    sum = 0
    for j in range(test_per_person):
        score = int(input("  Enter a score: "))
        sum = sum + score
    average = float(sum) / test_per_person
    print("     Average for " + name + ": " + str(round(average, 2)))

'''
Programmer: Andrew Gowan
Date:10.23.19
Program: Categories

This program will ask users of an interest to them
then ask for two items related to
that interest  
'''
for i in range(4):
    print("Outer For Loop: " + str(i))
    x = 6
    while x >= 0:
        print("    While Loop: " + str(x))
        x = x - 1 

