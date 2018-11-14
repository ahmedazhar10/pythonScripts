
#---------------PRINT HELLO WORLD----------#

print("Hello world")

print("    /|")
print("   / |")
print("  /  |")
print(" /   |")
print("/____|")

#------------------VARIABLE TYPES-----------#
character_name = "Tom"
character_age = 35
is_male = True
digits = 50.3425

print(character_age)
print("There once was a man named " + character_name)
print("He was " + str(character_age) + " years old")

#-----------------BUILT-IN FUNCTIONS-----------#

#String
phrase = "Giraffe Academy"
print(phrase.upper().isupper()) # Are all upper-case letters?
print(phrase[0]) # returns first element in phrase

#Integer
number = -5
print(number)
print(abs(number))
print(pow(5,3)) #5 ^ 3
print(max(4,6)) #prints large number
print(min(4,6)) #prints smaller number

#-------------RAW-INPUT-----------#

name = input("What's your name? ") #by default inputs are strings
age = input("And your age? ")
print("Hey " + name + "! Wow you're " + age + " years old!")

num1 = input("Num1")
num2 = input("Num2")
result = int(num1) + int(num2) #you could also do float(num1)
print(result)

#------------IF STATEMENTS-----------#

#Boolean if-statements

is_male = True
is_tall = True

if is_male and is_tall:
    print("You're a giant male")
elif is_male or is_tall:
    print("You're a man or tall or both!")
elif is_male and not(is_tall):
    print("Peter dinklage is that you?")
else:
    print("You're neither male nor tall!")

# Integer comparison if statments

chips = 5
my_pocket = 5
if my_pocket > chips:
    print("Go buy it son!")
elif my_pocket == chips:
    print("Go buy it son!")
else:
    print("You're going hungry tonight :(")

#--------------------------LOOPS--------------------------#

# WHILE LOOP
i = 1
while i <= 10:
    print(i)
    i += 1

print("Done with loop")

# FOR LOOP

for index in range(3):
    print(index) #0, 1 , 2

#Loop through a List
friends = ["Jim", "Karen", "Kevin"]
for friend in friends:
    print(friend)

#--------------------------FUNCTIONS------------------#

#Defining Function
def sayhi():
    print("Hey")

#Calling Function
sayhi()

#Using a Return statement
# def cube (number):
#     return number*number*number
