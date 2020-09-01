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
  Strings, often refered as text, need to be written betweed quotation marks. It doesn't matter if you use single `variable = 'Hello World!'` or double `variable = "Hello         World!"` unless you need to write quotation marks inside the actual string, then, we would use something like this `variable = "He said: 'Hello!'"` or something like this `variable = """He said: "Hello!""""`. It is important to use quotation marks when we want to treat the variable as text so that `string = "3"` is not equal as `number=3`. You will find more practical examples on the .py file for clarifiation. Using quotation marks also prevents us from assigning a variable to another, we'll cover this more in depth in a moment but here's an example: `hello = "I'm learning to code"` --> This variable contains `I'm learning to code` so if we do `variable = hello` instead of `variable = "hello"` The variable would contain `I'm learning to code` instead of `hello` 
  
  
  
## DISPLAYING VARIABLES
## MULTI-ASSIGNMENT 
## INCREASING AND DECREASING THE VALUES OF A VARIABLE

## GENERAL TIPS
