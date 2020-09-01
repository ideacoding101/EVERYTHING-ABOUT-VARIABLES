# EVERYTHING-ABOUT-VARIABLES
Take this repo as a blog post where I explain everything a beginner needs to know about variables. I also incluede a python file that contains all sorts of practical examples and clarifiacations of every topic we will discuss over this post.

## INDEX

## DEFINITION AND SYNTAX
Variables are used to store information to be referenced and manipulated in a computer program. They also provide a way of labeling data with a descriptive name, so our programs can be understood more clearly by the reader and ourselves. It is helpful to think of variables as containers that hold information. Their sole purpose is to label and store data in memory. This data can then be used throughout your program. As we referenced before, variables need to be labeled and despite other programming lenguages, in python they are declared at the same moment they are assigned. This leads us nicely to the syntax we use which is the following: `variablename = value`. You can see some practical examples on the .py file on this repo, but as you can see, we give the variable a name and then with the equal sign, we assign it a value. However, we can't use just any name, or any value. Keep reading to learn about that.

## VARIABLE NAMES
When it comes to giving a name to a variable there are some things that must be done, and some others that are a good practice, here's a list of both:

  ### A VARIABLE MUST OR MUSTN'T:
  * You can't name a variable using a number at the beginning, the program will crash
  * A variable musn't use a reseverd Python keyword as a name
  * You could actually use an undescore (`_`) at the starting of a variable, it looks weird but it's valid
  * If you declare an important variable, one that you are gonna use a lot, it's a must to give it a decriptive name, try to avoid things like:
      * variable1
      * thing
      * aasdasd
   
    And use names that will allow you to identify what the variable contains:
      * client_name
      * available_colors
      * result
      
   ### A VARIABLE SHOULD
   * Use only lower case letters  
   * Use an underscore at the beggining of the variable to distinguish it from the other
   * Try to use short and consice names
   * if you have to use more than one word, use underscores as a space indicator
   * Sometimes is a good idea to indicate the data type of the variable on its name
   * Try to use the same kind of cases for all your variables
   
  BEAR IN MIND THAT... Variable names are case sensitive, can only contain alphanumeric characters and underscores and they have an unlimited lenght.
  
   ### TYPES OF CASES
   * myVariable : Camel case --> Mainly used in Java
   * MyVariable : Capital camel case 
   * my_variable : Snake case --> Use this one for Python
   * my-variable : Kebab case --> Mainly used for URL's
   * variable : Flat case 
   * VARIABLE : Upper case --> Mainly used in C

## VARIABLE VALUES
You can assign many data types to a variable, in the following part, we'll name the most famous ones and we'll discuss in depth the most basic and important
  ### STRINGS
  Strings, often refered as text, need to be written betweed quotation marks. It doesn't matter if you use single `variable = 'Hello World!'` or double `variable = "Hello         World!"` unless you need to write quotation marks inside the actual string, then, we would use something like this `variable = "He said: 'Hello!'"` or something like this       `variable = """He said: "Hello!""""`. It is important to use quotation marks when we want to treat the variable as text so that `string = "3"` is not equal as `number=3`. You   will find more practical examples on the .py file for clarifiation. Using quotation marks also prevents us from assigning a variable to another, we'll cover this more in depth   in a moment but here's an example: `hello = "I'm learning to code"` --> This variable contains `I'm learning to code` so if we do `variable = hello` instead of `variable =       "hello"` The variable would contain `I'm learning to code` instead of `hello` 
  ### NUMBERS
  In basic python, we have two main types of numbers, there's obviously more but we won't use them until we discuss more advanced topics. We have integers or int such as `3` and   floats such as `3.5`. We can store these in variables as well but without using quotation marks `variable = 3`. This usually leads to confusion because we can also treat this   numbers as strings by putting quotation marks between them. However, if we wanna do mathematical operations, adding `"3"+"3"` will result in 33 because the quotation marks     indicate that we are dealing with strings and when we add strings we literally put one next to the other. However, when we add 2 integers, for instance `3+3` we get 6 because we  didn't use a string, we did the operation with integers. The same works with floats, we'll talk about operators and adding different datatypes in another article, just stick   with the syntax difference and the way they behave.
  ### BOOLEANS AND OTHERS
 With those two we would cover the basics but it's important to know that you can store lists, tuples, dictionaries, objects and many complex data types into variables. Also, even though we will dedicate an exclusive article about booleans it's great to know that variables can also store them. A boolean can be either True or False, 1 or 0, on or off. We write these on Python with `boolean_variable = True` or `boolean_variable = False`. Remember that we don't use quotation marks because we are the variables hold a boolean and not actual text.
  
## DISPLAYING VARIABLES
  ### PRINT()
  This is a rather simple topic that we might have already discussed over this article but when it comes to real practical python, we want to be able to output and display to our screen or console, our varibles. To do that, we use the built-in python function `print()`. To pass in a value or a variable we write it between those parenthesis: 
  * `print("Hello World!")`--> Here we display a string
  * `print(3)` --> Here we display a number as an integer
  * `pritn("3")` --> Here we display a number as a string or text
  * `print(variable)` --> Here we print out a variable, however, we need to create that variable before we use print (check the .py file for real examples).
  ### INPUT()
  Apart from the print function, there's another one called input() that is also pretty useful. It works in a similar way as print, take the input function as a question if you write to your code: `input("What's your age?")` it will display in the console the question and will ask the user for a reply. Put into the parenthesis a string that contains the question and the user will be forced to answer. However in this case, the user's reply won't be stored anywhere, to make this more useful you could use a variable: `user_answer = input("What's your name?")`. The way this works is when you run the program, the question will appear into your screen, after you answer, your answer will be stored into the variable, then you can print the variable for some really cool stuff. 
  ### COMBINING VARIABLES
  We can take this into the next level by combining all the things we've learned so far and the `+` operator. The `+` allows us to add either numbers or strings. If we print two numbers with `+` we will get the result of adding them: `print(3 + 3)` which is 6. However, we can also use it with strings: `print("Hello " + "World)` which will combine the two strings into one and we will get `Hello World`. Bear in mind that we add a space after `Hello ` so that the output is not `HelloWorld`. We can also add variables to this som imagine that the variable `word` contains the string `Hello ` we could: `print(word + "World")` and we would get: `Hello World`. Take a moment to assimilate all this knowledge and make sure you understand when to use "" (when we pass a string) and when they are not needed (When we reference an existing variable). Now, if we take this furthis, we can chain the variables, print, input and this last thing we've learned to crea somethings that prints a name depending on the user input, you can find this on the .py file. The way it works is basically you create a variable with the user's name based on their input `user_name = input("What's your name?")` and now we print it combined with another string: `print("Hello " + user_name)`
  
## MULTI-ASSIGNMENT 
## INCREASING AND DECREASING THE VALUES OF A VARIABLE

## GENERAL TIPS
