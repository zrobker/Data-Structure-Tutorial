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

[Back to Welcome Page](0-welcome.md)
