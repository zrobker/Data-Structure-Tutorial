# Stacks

## Introduction

When programming you will be working with a lot of data, and you need to be able to manipulate and organize that data in different ways. One of those ways is using Stacks. Stacks are data structures that work much like a stack of anything in the real world would, where you add something to the top and that top item is then the first to be removed. This is often called "LIFO" (Last In, First Out). Below we will see the various task we can accomplish with stacks when working with lists in Python.

## Last in First Out

To demonstrate this process the easiest way to understand is to imagine a stack of pancakes. Everytime you finish making another pankcake it goes on top of the stack of pancakes. Then when someone is ready to eat another pancake you will remove the top pancake and put it on thier plate. 

## Functions Associated with stacks

- `empty()`  : Returns if the stack is empty or not
- `size()` : Returns the size of the stack
- `push(value)` : Inserts the value on top of the stack
- `pop()` : Removes the top value of the stack


Here are some examples of each Function in Python:

```python
#Creates empty list
stack = []

#Push(Value)
stack.append(1)
stack.append(2)
stack.append("a")
stack.append("b")

#Size()
length = len(stack)

#Pop()
value = stack.pop()

#Empty()
if len(stack) == 0:
```

## Multiple Conditions

When we allow the software to make decisions, there might be more than one decision that should be made.  Specifying multiple conditions in python uses the `elif` and `else` keywords.  The `elif` keyword means "else if" and represents an additional condition.  The `else` keyword represents all other possible conditions.  Here is a complete example to consider:

```Python
if temp <= 32.0:
	print("Watch for ice!")
elif temp <= 50.0:
	print("Might want to bring a jacket!")
elif temp <= 80.0:
	print("What a beautiful day!")
else:
	print("Its warm out there ... look for some shade!")
```

When this code runs, if will first consider the `temp <= 32.0` condition.  If its True, then it will run the code within the block but then skip all the other conditions.  If the first condition was False, then it will consider the second condition `temp <= 50`.  Notice that in this second condition, we can assume that the temperature is already great than 32.0 because the first condition failed.  If none of the first 3 conditions result in a True (perhaps the temperature is balmy 90 degrees), then the `else` condition will result in True.  Notice that we never put a boolean condition next to the keyword `else`.

Sometimes programmers think they always need to put an `elif` and an `else` when they write an `if` statement.  This is not true.  You should think about all the scenarios you want to check for and use the `elif` and `else` as needed.  If we wrote the same code above  but without `elif` and `else`, we would have to write more complicated boolean expressions.  It is better to use `elif` and `else` to simplify the code and ensure the result we want.

## Example : Geometry Calculator

In the example below, we will write a simple Geometry Calculator.  Before we write the code, we should first think about what we want the software to do.  Writing a list of requirements is an important step in writing software.  The requirements can help us ensure that we using conditionals correctly.  

Geometry Calculator Requirements:

- Allow the user to select the shape they want to calculate the area for
- Ask the user for the size information of the shape they selected
- Ensure that size lengths are all valid (greater than zero)
- Display the results

```python
import math

print("Welcome to the Geometry Calculator")
print("Please select a shape:")
print("1) Square")
print("2) Triangle")
print("3) Circle")
choice = int(input("> "))  
if choice == 1:
    side = float(input("Side length of the square: "))
    if side > 0:
        area = side ** 2
        print("The area is {}".format(area))
    else:
        print("Invalid side length!")
elif choice == 2:
    base = float(input("Length of the triangle base: "))
    height = float(input("Length of the triangle height: "))
    if base > 0 and height > 0:
        area = 0.5 * base * height
        print("The area is {}".format(area))
    else:
        print("One of the lengths was invalid!")
elif choice == 3:
    radius = float(input("Raidus of the circle: "))
    if radius > 0:
        area = math.pi * radius * radius
        print("The area is {}".format(area))
    else:
        print("Invalid radius length!")
else:
    print("Invalid Menu Selection")
```

Note the use of `elif` to provide conditions for different choices and `else` for the special condition of an invalid choice.  Within each conditional block, different prompts, variables, expressions, and conditionals are used.

## Problem to Solve : Summer Camp Cost

Write a program that will determine the cost for a child to attend a summer camp based on various factors described below:

The base cost of attending summer camp is determined by the age of the child:

|   Age   |      Cost      |
| :-----: | :------------: |
| Under 8 | Can not attend |
|  8-10   |     $1000      |
|  11-12  |     $1500      |
|  13-16  |     $2000      |
| Over 16 | Can not attend |

The base cost is reduced based on the number of children (of any age) in the family and the family income:

| Family Income        | 1 Child in Family | 2 Children in Family | 3+ Children in Family |
| -------------------- | ----------------- | -------------------- | --------------------- |
| Under 25K per Year   | - 70%             | - 80%                | - 90%                 |
| Under 50K per Year   | - 40%             | - 50%                | - 60%                 |
| Under 75K per Year   | - 10%             | - 20%                | - 30%                 |
| 75K or More per Year | No Reduction      | No Reduction         | No Reduction          |

You can test your program with the following scenarios:

- Test 1: 10 year old, 2 children in the family, family income 45K per year will cost: $500 (50% off)
- Test 2: 14 year old, 3 children in the family, family income 70K per year will cost: $1400 (30% off)
- Test 3: 12 year old, 1 child in the family, family income 80K per year will cost: $1500 (0% off)
- Test 4: 18 year old, 3 children in the family, family income 23K per year will cost: N/A - They can't attend

You can check your code with the solution here: [Solution](summer_camp_cost.py)



[Back to Welcome Page](0-welcome.md)
