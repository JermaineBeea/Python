# Functions in Python

**Instructions:**

1. Fork this repository to your own Gitlab account.
2. Clone the forked repository to your local machine.
3. After completing each exercise: git add, git commit, and git push to your forked repository.

## Table of Contents
1. [Functions](#functions)
2. [Function Parameters](#function-parameters)
3. [Function Scoping](#function-scoping)
4. [Return Values](#return-values)
5. [Recursion (Detour)](#recursion) 
6. [The Main Program](#the-main-program)


## Functions

**What are functions?**

Functions are blocks of reusable code that perform a specific task or set of tasks.
They are defined using the `def` keyword followed by a function name and parentheses.

```python
#Functions
                                def
#Defined using the above keyword
#The anatomy/syntax of a function

def name_of_the_function(): #Function is defined
    #The function will implement the code that goes under it. (Mind The Indentation)
```

```python
#Let's put it into practice
#Run the code below and see what you get

score = 9

def update_score(): #Function is defined
    """This function takes the variable 'score' declared above and increases the score by 1"""
    score +=1

print(score)

#What's the score now? Explain why...

-------------------------------------------------------------------------------------------------

#Let's try this again
#Run the code below and see what you get

score = 9

def update_score(): #Function is defined
    """This function takes the variable 'score' declared above and increases the score by 1"""
    score +=1

update_score() #Function is being called

print(score)


#What's the score now? Explain why... 
#What's the difference between the two blocks of code above?
```

Let's look at another example of creating functions

```python
#Let's put it into practice
#Run the code below and see what you get

def print_hello_world():
    print("Hello World")

#What happens when you run the code? Why ...

-------------------------------------------------------------------------------------------
#Let's try this again
#Run the code below and see what you get

def print_hello_world():
    print("Hello World!")

print_hello_world()

#What happens when you run the code now? Explain why... 
#What's the difference between the two blocks of code above?
```

By using functions effectively, you can create organized and maintainable code, making your programs more efficient and easier to manage.

## Function Parameters

**What are function parameters?**

Function parameters, also known as function arguments, are values that you pass to a function when you call it. These parameters allow you to customize the behavior of a function and provide data for the function to work with. 

Function parameters are specified within the parentheses'()' of a function's declaration.

```python
#Parameters
#The anatomy/syntax of a function with a parameter
                    def some_function(this_is_a_parameter): #The parameter serves as a variable

                        #'this_is_a_parameter' is a variable that can ONLY be recognised inside this function
                        print(this_is_a_parameter)  

```

Let's see how this works. Let's create a function that greets the user :smile:

#STAGE 1

```python
#Let's put it into practice

def print_welcoming_message():
    """
    Function Greets the user with a message.
    """

    print("Hey User!, Welcome to the world of coding!")

print_welcoming_message()

#Explain the code above with your neighbour ...

```

------------------------------------------------------------------------------


Let's greet the user by their name, who likes to be called by 'User' anyway :rolling_eyes:

#STAGE 2
```python
#Let's try again
#Run the code below and see what you get

def print_welcoming_message(username): 
    """
    Function Greets the user with a PERSONALISED message.

    Parameters:
    username (str): The name of the user.
    """

    print(f"Hey {username}! Welcome to the world of coding!")


name = "Zakumi" #This is a declared variable assigned to the value 'Zakumi'

print_welcoming_message(name) #We call the function and PASS the variable defined above 'name' directly into the function as an ARGUMENT

```
Let's explain how this argument vs parameter thingy works
```python
#Let's visualise this

some_variable = "Zakumi" #The value will be the argument that is passed through the parameter that was defined in the function
                        
some_function(some_variable)



def some_function(this_is_a_parameter):
                            |          #This is how it kinda looks in the background
                            |          #The parameter-variable 'this_is_a_parameter' is assigned to the argument that's being passed above    
                            |           this_is_a_parameter = "Zakumi" #The value being PASSED into the function is 'Zakumi'
                            -------------
                                        |
                                        v
    print(f"print variable/argument: {this_is_a_parameter}") #Prints

```

We now understand how values are passed as arguments through parameters which are declared in functions :smile:

Now... How many parameters can go on one function? Mmmhhhh :thinking: Let's test this out..

#STAGE 1

```python
#Let's put it into practice
#Run the code below and see what you get


def sum(a):
    print(a+5)


num1 = 2

sum(num1)

#This function has one parameter, this means...... it takes in once argument


``` 

#STAGE 2

```python
#Let's put it into practice
#Run the code below and see what you get 

def sum(a,b):
    print(a+b)

num1 = 2
num2 = 5

sum(num1,num2)


#This function has two parameters, this means...... it takes in two arguments, i.e num1 and num2

``` 

#STAGE 3

```python
#Let's put it into practice
#Run the code below and see what you get 

def sum(a,b,c):
    print(a+b+c)

num1 = 2
num2 = 5
num3 = 3

#We'll leave it to you to call the function and and pass the arguments under this line 


#This function has THREE parameters, this means...... it takes in THREE arguments, i.e num1, num2 and num3
```

You can have any number of parameters in a function. There is no strict limit on the number of parameters a function can accept. However, it's important to consider code readability and maintainability.

Having too many parameters in a function can make the code complex and hard to understand. In such cases, it's advisable to reconsider the design and structure of your code.


One way to improve your skills is familiarising yourself with different kinds of errors

Now let's check this out...

```python 
#Let's put it into practice
#Run the code below and see what you get

def print_user_details(name,surname)
    print(f"My name is {name} {surname} and I enjoy gaming as a hobby")

n = "Zakumi"

print_user_details(n)

#What do you get? 
#we'll leave it to you to fix it

------------------------------------------------------------------------------------------

#Let's put it into practice
#Run the code below and see what you get

def print_user_details(name,surname)
    print(f"My name is {name} {surname} and I enjoy hobby as a hobby")

n = "Zakumi"

s = "Ngwenya"

print_user_details(name,surname,hobby)

#What do you get? 
#we'll leave it to you to fix it
```


## Function Scoping

We will now shift our attention to examining how declared variables impact functions. There are two distinct types of variables to consider: **global variables** and **local variables**.

**Global Variables**

Variables declared outside any function are known as global variables. These variables have a global scope, meaning they can be accessed from anywhere in the program. Global variables persist throughout the program's execution and can be modified by any part of the code.

```python
#Let's put it into practice
#Run the code below and see what you get

this_is_a_global_variable = 10

def function_using_global_var():
    print(f"Accessing global variable: {this_is_a_global_variable}")

# The global variable is accessible here
function_using_global_var()
```

**Local Variables**

Variables declared inside a function are referred to as local variables. These variables have a local scope, meaning they are only accessible within the specific function where they are declared. Local variables are temporary and exist only for the duration of the function's execution.

```python
#Let's put it into practice
#Run the code below and see what you get

def function_with_local_var():
    this_is_a_local_variable = 5
    print(f"Accessing local variable: {this_is_a_local_variable}")

# The local variable is only accessible within the function
function_with_local_var()

-------------------------------------------------------------------------------------

# Attempting to access the local variable here would result in an error

#TODO

# print(f"Trying to access local variable outside function: {this_is_a_local_variable}")

```


What's the best practice?
1. Avoid Overusing Global Variables:   
While global variables provide a way to share data, it's generally a good practice to minimise their use to prevent unintended interactions.

2. Use Parameters for global-Scoped Data:       
Pass data to functions through parameters rather than relying on global variables. This makes functions more structured and easier to test.


Understanding the distinction between global and local variables is crucial for writing clean and maintainable code


## Return Values
**What are return statements?**

In programming, return statements are a key component in functions. They enable a function to send a specific value back to the code that called it. This mechanism allows functions to produce results or outcomes that can be utilized in the broader program. Return statements also play a role in controlling the flow of a program by terminating the execution of a function when encountered. 


```python
#Return Statements
                                return
#Uses the above keyword


def some_random_function():
    #The function will implement the code that goes under it. (Mind The Indentation)

    return #Return statement is used INSIDE the function (Mind the indentation)
```


As mentioned above, return statements have two main uses and we'll now delve into them.


1. **Function Termination:**

Return statements also serve as a mechanism to terminate the execution of a function. When a return statement is encountered, the function stops executing, and any code after the return statement is skipped.

```python
#Let's put it into practice
#Run the code below and see what you get

def check_number(num:int):

    if num < 0:
        print("The number is negative")
        return
    elif num > 0:
        print("The number positive")
        return
    
    print("The number is zero")

#What do you get? 
#Does the function terminate? Yes/No? Why? How?
#we'll leave it to you to discuss this with your peers

-----------------------------------------------------------------
#What's the difference between the above block of code compared to the one below

def check_number(num:int):

    if num < 0:
        print("The number is negative")
        return
    elif num > 0:
        print("The number positive")
        return
    
    else:
        print("The number is zero")
```

2. **Value Output:**

Return statements are employed to provide a value as the output of a function. This value is sent back to the code that called the function, allowing for dynamic and result-oriented behavior.

In simpler terms, return statements are used to 'store' data from a particular function after it has executed/called. 

```python
#Let's put it into practice
#Run the code below and see what you get

def check_number(num:int):

    if num < 0:
        print("The number is negative")
        
    elif num > 0:
        print("The number positive")
    
    return print("The number is zero")


number = 234

check_number(number)

#What do you get? 
#Does the function return the correct statement? Yes/No? Why? How?
#we'll leave it to you to discuss this with your peers and fix it ;)

#Hint, print function and return statement are NOT the same thing
```

Functions that return some values act as storages. See below

```python
#Let's put it into practice
#Run the code below and see what you get

def some_function():

    #Code will execute as expcted  

    return "This random function returns this string"
                    
                    |
                    |
                    |
                    |
                    v
value_stored_from_function_saved_in_variable = some_function()  #Call the function

print(value_stored_from_function_saved_in_variable)

#What do you get? 
#Does the function return the correct statement? Yes/No? Why? How?
#we'll leave it to you to discuss this with your peers
```

## Recursion

Let's take a bit of detour and talk about recursion.

**What is recursion?**

Recursion is a programming concept where a function calls itself in order to solve a problem. It's like a task asking a smaller version of itself to help out until the task becomes so small and straightforward that it can be easily solved.

```python
#The anatomy of a recursive function

def some_function(some_argument):

    if some_argument <= some_predetermined_limit: #This is called a base case check
        # Do something and terminate
        
    else:
        # Function will execute
        some_function(some_argument_modified) #This is a recursive call
```

-  ***Base Case Check:*** Inside the function, there's an if statement checking if some_argument is less than or equal to a certain limit (determined_some_limit). This is known as the base case. If this condition is met, the function performs some specific actions and then terminates.

-  ***Recursive Call:*** If the base case is not met (i.e., some_argument is greater than the limit), the function goes to the else block. Inside the else block, the function calls itself (some_function) with a potentially modified argument (some_argument_modified). This is the recursive step

**NOTE: It's important to ensure that with each recursive call, the function moves towards the base case, where it can eventually terminate. If this condition is not met, the function will keep calling itself indefinitely, leading to a situation known as "infinite recursion."**




```python

#Let's put it into practice
#Let's start with a while loop
#Write a while loop that counts down from a user-specified number to 0 and prints "Blastoff!"

while something_something: 

    #Blah blah blah


------------------------------------------------------------------------------------

#Let's do the same thing recursively

def count_down(n):

    if 'basecase check':
        print("Blastoff!")

    else:
        #Do something here
        count_down('modify me here')

# Call the function with 5 as the starting point
count_down(10)

```

That's the end of our detour.

## The Main Program

**What is it?**

This refers to the central part of a software application. This is where the *CORE LOGIC* is organised and executed. The main program is responsible for orchestrating different components, handling user input, and driving the *OVERALL FUNCTIONALITY* of the software.

```python

#The anatomy of the main 

if __name__ == "__main__":
    do_something() #Mind the indentation

    saved_here = do_another_thing()

    do_another_that_depends_on_do_another_thing(saved_here)

```

Now... Let's break this down a bit. 

**Why is this important?**

There's a few reasons why it's important to have the main in your programme.

1. ***Assists with logic (Organisation):*** The main program is often responsible for coordinating the flow of execution.
It calls various functions or methods to perform specific tasks and achieves the overall goal of the program. 

2. ***Integration of modules (Central hub):*** Programs are typically modular, consisting of multiple functions, classes, or modules.
The main program integrates these modules, calling their functions or methods to achieve the desired functionality. (More detial in the module workshop)

3. ***Initialisation (Entry point):*** The main program often takes care of initializing necessary resources (variables, data structures, connections) before the core logic starts.

These are only but a few important uses of the main program.

Conclusion
--


By following this order, you will build a strong understanding of functions in Python. Make sure to commit your changes and push them to your forked repository after completing each exercise. Enjoy the learning experience!

