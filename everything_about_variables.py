print("#---------------EVERYTHING ABOUT VARIABLES by ideacoding---------------#")

print("#SYNTAX#")

number = 3      #This variable called number is assigned the numer 3 by the = operator
name = "Chris"  #Here you have some more examples, we'll cover about this later but you see the syntax right?
is_admin = True
result = 3.5

print("#---------------------------------------------------------------------#")

print("#VARIABLE NAMES#")

# 3variable = "This won't work"     #A number in front of a variable will crash the program
# class = "This won't work either"  #Class is keyword that python uses so, we can't name a variable using it
_class = "This is a valid name"     #If you really need to use a keyword as a name, put an underscore in front of it

variable1 = "Tim"                   #Try to avoid using the following names, they can sometimes be confusing
thing = 3453
asdfsadf = "Chris"

client_name = "Mathew Harris"       #This ones are much better!
available_colors = 5                    #-Lower case
result = "Positive"                     #-Concise and short
                                        #-Uses underscores for spaces
                                        #-They all use the same case

myVariable = "Camel case"
MyVariable = "Capital camel case"
my_variable = "Snake case"
#my-variable = "Kebab case"
variable = "Flat case"
VARIABLE = "Upper case"

print("#---------------------------------------------------------------------#")

print("#VARIABLE VALUES#")

variable = "Double quotes are fine"               
variable = 'Single quotes are fine'

variable = "We can write 'quotes' inside a string"
variable = 'They just need to be "different" from the opening and closing ones'

string = "3"                        #This is a sting which means this is treated as text

number = 3                          #This is an integer which means this is treated as a number

print(number)                       #If we print them, they look the same...
print(number)

print(string + string)              #However, when we add them, they behave differently
print(number + number)

hello = "I'm learning to code"      #Run this and see how the output changes depending if we use quotation marks or not
print(hello)
print("hello")

variable_float = 4.5                #We also have decimal numbers
variable_boolean = True             #And booleans

print("#---------------------------------------------------------------------#")

print("#DISPLAYING VARIABLES#")

print("Hello World!")               #We display text by using the print function and passing a string as a perameter
print("3")                          #We display a number as a string, we've seen before the different interactions with the + operator
print(3)                            #We display a number
variable = "Hello"                  #We declare a variable and we put a string inside
print(variable)                     #We print a variable we've declared before
print("variable")                   #Here we print the same as before but betweed quotation marks(which means it's treated as a string) run the code and see the diference

#input()                            #This displays an input form without text
#input("What's your name")          #This displays an input form with some text as a question
#user_reply = input("Enter your age")#This will store the input of the user(his age) inside the variable

print(3+3)                          #We add two integers
print("Hello " + "World")           #We add two strings
print("Hello" + "World")            #We need to put a space after hello or before world, check the output of this code and see the diference
#print(3 + "Hello")                 #This is not valid
word = "Hello "                     #The variable contains hello
print(word + "World")               #We combine the variable and the string World
user_name = input("What's your name?")#This stores the name of the user in the variable
print("Hello " + user_name)         #We pring hello and we add the name of the user right after that
greet = "Hello"                     #We create a variable that stores hello
user_name = input("What's your name?")#We ask the user for their name and we store it
print(greet + user_name)            #We combine the last two variables and we obtain the same result

print("#---------------------------------------------------------------------#")

print("#MULT-ASSIGMENT#")

x, y, z = "Bob", "Alice", "John"    #Each variable is set to their corespondent value
print(x)
print(y)
print(z)

x = y = z = "Bob"                   #All the variables are set to bob
print(x)
print(y)
print(z)


variable1 = 4                       #We can assign a variable to another variable
variable2 = variable1
print(variable2)

print("#---------------------------------------------------------------------#")

print("#INCREASING AND DECREASING THE VALUES OF A VARIABLE#")

points = 20                         #This is a good way of increasing a variable by 10
points = points + 10
print(points)

points = 20                         #However, this is much better and faster
points += 10
print(points)

lives = 3                           #It also works with the - operator
lives -= 1
print(lives)

print("#---------------------------------------------------------------------#")










