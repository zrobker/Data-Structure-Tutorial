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
You can then use these built in functions to word with sets:

- `set.add(value)`  : Adds value to set
- `set.remove(value)` : Removes value from set
- `if value in set:` : You can use a simple if statement to check if the value exists in the set
- `len(set)` : Finds number of items in the set

## Intersection

One of the main uses of sets is the ability to perform mathematical operations with them. One operation is finding which data is found within various sets or the `intersection`.

```python
#two different sets and thier data
set1 = {1,3,5,6,7}
set2 = {1,3,4,7,8}

#there are two ways to find the interestion 
set3 = intersection(set1,set2)
set3 = set1 & set2

#each of these if implemented correctly should return this
{1,3,7}
```

## Union

Another operation is refered to as `union`. This means to sift through all the data in 2 or more sets and combing it all together without having repeating values. 

```python
#two different sets and thier data
set1 = {1,3,5,6,7}
set2 = {1,3,4,7,8}

#there are two ways to find the interestion 
set3 = union(set1,set2)
set3 = set1 | set2

#each of these if implemented correctly should return this
{1,3,4,5,6,7,8}
```

## Example : Party Problems

Kevin is going throw a party but can only invite 10 people. He wants to invite everyone but thinks he will have too many people. So he divided his friends into groups to see who would enjoy the party more. He has two groups those who like pizza and those who like star wars. He first want to invite those who like both pizza and star wars then others if he still can. We are going to help him by using sets.

```python
#create and populate sets
like_pizza = {"Jim","Bob","Jess","Sarah","Zach","Dwayne","Vanessa","Josh","John","Rob","Juan","Chloe","Chris","Tim","Nick"}
like_star_wars = {"Jim","Chris","Steph","Rob","Tay","Dwayne","Jenifer","Josh","Anne","Tim","Joe","Juan"}

#union of two sets (gives us a list of every friend and no duplicates)
everyone = like_pizza | like_star_wars

#intersection of two sets (his friends who like both pizza and star wars)
invite = like_pizza & like_star_wars #{'Tim', 'Chris', 'Jim', 'Josh', 'Juan', 'Rob', 'Dwayne'}

#function created to make sure 10 friends are going to be invited
def invite_10(invite, everyone):
    for person in everyone:
        #check length of set to make sure we dont get more than 10 friends
        if len(invite) >=10:
            return print(invite)
        #if we dont have 10 yet we add one from the set of everyone
        else:
            if person not in invite:
                invite.add(person)

#the fuction will return a list of people Kevin should invite 
invite_10(invite, everyone) #{'Bob', 'Tim', 'Steph', 'Chris', 'John', 'Jim', 'Josh', 'Juan', 'Rob', 'Dwayne'}

```

## Problem to Solve: Company Merger

Two clothing stores have decided to merge to become a new store. Each store has thier own perk members that recieve a weekly email with deals and news. It is your job to combine each stores data and to make sure that no one is recieving multiple emails you will use sets to prevent duplicates. The stores also want to reward anyone that might have a membership with both stores by sending them a special email with bonus deals thanking them for shopping at both establishments previously. 

You will need to accomplish this without using the built in python fuctions for intersection and union (using `&` or `|` as seen in the example above).


You can compare your code with the solution here:[Solution](2-solution.py)

[Back to Welcome Page](0-welcome.md)