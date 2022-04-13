# Trees

## Introduction

Binary Trees are another great way to store and manipulate data. To understand how a binary tree functions we will refer to the image below. When using this data structure we can link or connect data together, as seen in the image each piece of data is saved in what we call a `node`. The top node of the tree is called the `root` and the bottom nodes are called `leaves`. A node that has connected nodes below it is also refered to as `parent` and the nodes below a `child` node.
![Binary Tree](tree.jpg)

## Binary Search Trees

Using the same image above we will discuss binary search trees. When placing data into the tree we will compare it to the parent nodes. We will always start at the root node and go left if the data is smaller or right if the data is larger. In the image the root node 8 was placed first then all aditional data was compared one by one and set into place. If we were to place 9 into the BST we would start by comparing it to the root. 9 is greater than 8 so we would then move right and compare 9 and 10. 9 being less would then be placed to the left of 10 and become a leaf and a child to 10. This process can work in O(log n) time when implemented correctly and when the tree is balanced.

## Balanced vs Unbalanced

An easy way to understand balanced vs unbalanced is to think of an old counter weight scale where you need equal weight on each side to balance the scale. A trees balance depends on the order in which the data is entered. The tree above is an example of a balanced tree we can assume the data was entered in an order such as: 8,3,10,6,14,1. Whereas an example of an unbalanced tree would be entered like this: 1,3,6,8,10,14. When entered in this way the root would be 1 and each number after going to the right. If a tree is unbalanced it will perform slower in O(n) time.

## BST Operations

First in order to understand the operations we can perform with BSTs we have to understand what `recursion` is. Recursion is basically writing code that involves a function calling itself. Below is a simple example of recursion.

```python
#here we have a function that will count down 1 by 1 from any number given 
def count_down(number):
    #recursion requires that we have a base case to make sure the function does not run forever
    if number <= 0:
        return
    else:
        print(number)
        #here we are calling the function inside itself and subtracting one from the number parameter given
        count_down(number-1)
```
The two main operations we can perform are `inserting` into a BST and `Traversing` through a BST. Examples of both can be seen below.

```python
#Inserting
def insert(self, data):
	
	if self.root is None:
		self.root = BST.Node(data)
	else:
		self._insert(data, self.root)  # Start at the root

def _insert(self, data, node):

	if data < node.data:
		# The data belongs on the left side.
		if node.left is None:
			# We found an empty spot
			node.left = BST.Node(data)
		else:
			# Need to keep looking.  Call _insert
			# recursively on the left subtree.
			self._insert(data, node.left)
	elif data >= node.data:
		# The data belongs on the right side.
		if node.right is None:
			# We found an empty spot
			node.right = BST.Node(data)
		else:
			# Need to keep looking.  Call _insert
			# recursively on the right subtree.
			self._insert(data, node.right)

#Traversing
def __iter__(self):
	
	yield from self._traverse_forward(self.root)  # Start at the root

def _traverse_forward(self, node):
	
	if node is not None:
		yield from self._traverse_forward(node.left)
		yield node.data
		yield from self._traverse_forward(node.right)
```

[Back to Welcome Page](0-welcome.md)