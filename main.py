from functools import reduce


# Attempt the questions, if you get stuck the answers are below, have fun! :)



#1 Capitalize all of the pet names and print the list







#2 Zip the 2 lists into a list of tuples, but sort the numbers from lowest to highest.






#3 Filter the scores that pass over 50%





#4 Combine all of the numbers that are in a list on this file using reduce (my_numbers and scores). What is the total?

































'''
Q1

my_pets = ['sisi', 'bibi', 'titi', 'carla']

def capitalize(string):
    return string.upper()

print(list(map(capitalize, my_pets)))

Q2

my_strings = ['a', 'b', 'c', 'd', 'e']
my_numbers = [5,4,3,2,1]

print(list(zip(my_strings, sorted(my_numbers))))

Q3

scores = [73, 20, 65, 19, 76, 100, 88]

Q4

def accumulator(acc, item):
    return acc + item

print(reduce(accumulator, (my_numbers + scores)))

'''