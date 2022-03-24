# Stacks

## Introduction

When programming you will be working with a lot of data, and you need to be able to manipulate and organize that data in different ways. One of those ways is using Stacks. Stacks are data structures that work much like a stack of anything in the real world would, where you add something to the top and that top item is then the first to be removed. This is often called "LIFO" (Last In, First Out). When talking about performance, stacks are expected to take O(1) time when inserting or deleting. Below we will see the various task we can accomplish with stacks when working with lists in Python.

## Last in First Out

To demonstrate this process the easiest way to understand is to imagine a stack of pancakes. Everytime you finish making another pankcake it goes on top of the stack of pancakes. Then when someone is ready to eat another pancake you will remove the top pancake and put it on thier plate. To accomplish this in a stack we will use built in python functions such as `push` to add to the stack and `pop` to remove from the stack.

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

## Example : Word Sorting

In the example below, we will write a simple Geometry Calculator.  Before we write the code, we should first think about what we want the software to do.  Writing a list of requirements is an important step in writing software.  The requirements can help us ensure that we using conditionals correctly.  

Geometry Calculator Requirements:

- Allow the user to select the shape they want to calculate the area for
- Ask the user for the size information of the shape they selected
- Ensure that size lengths are all valid (greater than zero)
- Display the results

```python
#This function will take in a string and return all the words that are 5 letters long
def find_5_letter_words(input):
    #creates an empty string
    stack = []
    #splits each word in string into separate item in list
    for word in input.split(' '):
        #adds each word to stack
        stack.append(word)
        #removes words depending on length
        if len(word) < 5:
            stack.pop()
        elif len(word) >= 6:
            stack.pop()
    #prints remaining words in stack
    for item in stack:
        print(item.capitalize())
    

random_words = "wow understandable up down dog outstanding hello part very drastic tale so now lisa wonderful bye property world stylishear back we saturn now rate are yelp"        
find_5_letter_words(random_words)
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
