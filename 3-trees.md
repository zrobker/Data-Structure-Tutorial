# Trees

## Introduction

Binary Trees are another great way to store and manipulate data. To understand how a binary tree functions we will refer to the image below. When using this data structure we can link or connect data together, as seen in the image each piece of data is saved in what we call a `node`. The top node of the tree is called the `root` and the bottom nodes are called `leaves`. A node that has connected nodes below it is also refered to as `parent` and the nodes below a `child` node.

![Binary Tree](tree.jpg)

## Binary Search Trees

Using the same image above we will discuss binary search trees. When placing data into the tree we will compare it to the parent nodes. We will always start at the root node and go left if the data is smaller or right if the data is larger. In the image the root node 8 was placed first then all aditional data was compared one by one and set into place. If we were to place 9 into the BST we would start by comparing it to the root. 9 is greater than 8 so we would then move right and compare 9 and 10. 9 being less would then be placed to the left of 10 and become a leaf and a child to 10. This process can work in O(log n) time when implemented correctly and when the tree is balanced.

## Balanced vs Unbalanced

I


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
#two different sets and their data
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
            invite.add(person)

#the fuction will return a list of people Kevin should invite
invite_10(invite, everyone) #{'Bob', 'Tim', 'Steph', 'Chris', 'John', 'Jim', 'Josh', 'Juan', 'Rob', 'Dwayne'}

```

## Problem to Solve: Company Merger

Two clothing stores have decided to merge to become a new store. Each store has their own perk members that receive a weekly email with deals and news. It is your job to combine each stores data and to make sure that no one is receiving multiple emails you will use sets to prevent duplicates. The stores also want to reward anyone that might have a membership with both stores by sending them a special email with bonus deals thanking them for shopping at both establishments previously. 

You will need to accomplish this without using the built in python fuctions for intersection and union (using `&` or `|` as seen in the example above).

Use the following code to test your code:

```python
company1 = {1,9,3,4}
company2 = {8,9,10}
print(intersection(company1,company2))  # output {9}
print(union(company1,company2)) # output {1, 3, 4, 8, 9, 10}

company1 = {"email@gmail.com","email@yahoo.com","email@hotmail.com","email@outlook.com","email@university.com"}
company2 = {"email@gmail.com","name@yahoo.com","name@hotmail.com","name@outlook.com","email@university.com"}
print(intersection(company1,company2))  # output {'email@gmail.com', 'email@university.com'}
print(union(company1,company2)) # output {'name@outlook.com', 'name@hotmail.com', 'name@yahoo.com', 'email@hotmail.com',
                                #'email@university.com', 'email@yahoo.com', 'email@gmail.com', 'email@outlook.com'}
```

You can compare your code with the solution here:[Solution](2-solution.py)

[Back to Welcome Page](0-welcome.md)