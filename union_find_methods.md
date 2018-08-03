union_find.py Methods
=====================

find_index / find_object
------------------------

- if object is not already present within union_find:
	- adds object to stringtoindex list
	- adds object to roots
- if the root of the object is itself, returns (index of) itself
- if the root of the object is something else, returns (index of) the root

union
-----

- calls find_index for both nodes
- sets the foot of the first node to the second node

get_roots
---------

- for each node in stringtoindex:
	- if its root is not alreay in simplifiedroots, adds its root's index to simplified roots
- changes each value from index to corresponding node's string using stringtoindex
- returns list of node names

get_encompassed_nodes
---------------------

- for each node in stringtoindex:
	- if the root of the node is the input object, adds to encompassed_nodes
- adds input object itself to encompassed_nodes
- returns list of encompassed nodes

Important Variables / Lists
=============================

- roots
	- stores the root of a node at the index that node has in stringtoindex
- stringtoindex
	- stores all the nodes put through the find methods