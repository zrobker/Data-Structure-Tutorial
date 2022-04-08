# Sets

## Introduction

Much like stacks, sets are a very useful way to work with data when programming. Althought, the two data structures have a few key differences. Unlike stacks, sets do not care about order and they do not allow any duplicate data to be entered. One very common example we can use to understand this concept is having a membership at a gym or other service. When you order a membership your name is added to the set and it can easily check to see if you have a membership by checking if your name is in the set. And ultimately if you stop paying for your membership your name is then removed from the set. Sets are expected to take O(1) time when adding, removing, or finding data within a set. Below we will see the various tasks we can accomplish with sets when working with lists in Python.

## Sets in Python

When creating sets you will use one of the following:

```python
#You will use a curly bracket when defining a set with data inside
set1 = {1,2,3,4,5}
#but when you create an empty set you must use code such as this
empty_set = set()
```
You can then use these methods to word with sets:

- `set.add(value)`  : Adds value to set
- `set.remove(value)` : Removes value from set
- `if value in set:` : You can use a simple if statement to check if the value exists in the set
- `len(set)` : Finds number of items in the set

## Intersection

One of the main uses of sets is the ability to perform mathematical operations with them. One operation is finding which data is found within various sets or the `intersection`.

```python
#two different sets and thier data
set1 = {1,3,5,6,7}
set1 = {1,3,4,7,8}

#
```

## Union

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