graphvizlayout.py graph & extended_graph Methods
==================================================

add_nodes
---------

- for each node in compressed_nodes:
	- if not part of a cluster, sets label to name
	- if part of a cluster, sets label to cluster + name
	- if only one node in graph, adds that node
	- if the node has any edges, adds that node

remove_edges
------------

- for each edge in compressed edges (and both nodes are in all_nodes if extended_graph):
	- if the root of both nodes is the same, removes edge

compress_edges
--------------

- for each edge in compressed_edges:
	- replaces nodes with their compression roots
- for each edge in compressed_edges
	- adds to final compression if it is not already there and if the roots of the two nodes are not the same (removes duplicates and edges from / to the same node)

graphvizlayout.py graph Specific Methods
==========================================

__init__
--------

- takes in file
- initializes important variables / lists and union_finds
- creates an instance of GraphViz

main
----

- calls find_nodes and find_edges
- removes nodes with no edges
- prints total number of nodes
- if user requests compression:
	- calls compress
- if user does not request compression:
	- fills compressed_nodes and compressed_edges with the fill list of nodes and edges
- calls add_nodes and add_edges

find_nodes
----------

- reads through equality lines and:
	- implements union_find to store all root nodes
- reads through direction lines and:
	- runs nodes through union_find in case they have not already been stored
	- sets all_nodes to the roots of union_find
	
find_edges
----------

- reads through direction lines and:
	- for each node to the left of the arrow, adds edge from that node to node right of the arrow if not already in all_edges

add_edges
---------

- adds edge to GraphViz setup for each edge stored in compressed_edges
	
compress
--------

- initialized compressed_edges to have all the edges
- while there is still more compression to be done:
	- makes boolean array with all nodes as true
	- for each node, if true:
		- compresses the two nodes of the edge and makes both nodes false
- sets compressed_nodes to roots of compressionu
- sets compressed_edges to compress_edges

graphvizlayout.py extended_graph Specific Methods
===================================================

__init__
--------

- takes in cluster root to be expanded, the first gen graph instance (for use of the union_find), and the most recent gen's compressionu
- initialized important variable / lists and union_finds
- sets all_nodes to the nodes encompassed by the given cluster root
- creates a new instance of GraphViz

main
----

- calls find_edges
- - if user requests compression:
	- calls compress
- if user does not request compression:
	- fills compressed_nodes and compressed_edges with the fill list of nodes and edges
- calls add_nodes and add_edges

find_edges
----------

- for each edge from the first gen edge list:
	- if either nodes is in current gen's all_nodes, adds to all_edges
	
compress
--------

- puts all nodes from the edges that are in all_nodes into the compressionu
- while there is still more compression to be done:
	- makes boolean array with all nodes as true
	- for each node, if true:
		- compresses the two nodes of the edge and makes both nodes false
- sets compressed_nodes to roots of compressionu
- sets compressed_edges to compress_edges

add_edges
---------

- for each edge in compressed_edges:
	- if both nodes are in compressed_nodes, adds edge to the GraphViz canvas
	- if one only one node is in compressed_nodes, adds the other node to the GraphViz canvas in purple and adds the edge to the GraphViz canvas

graphvizlayout Important Variables / Lists
============================================

- file
	- prs file given from graphing instance
- u
	- instance of union_find used to eliminate duplicate nodes while drawing
- compressionu
	- instance of union_find used during compression to merge nodes under a given root
- all_nodes
	- all of the root nodes from u
- all_edges
	- edge list from the prs file with all nodes changed to their root nodes from u
- c
	- instance of GraphViz for drawing
- compressed_nodes
	- if the user indicates compression, compressed_nodes is the list of roots after the compression has taken place
- compressed_edges
	- if the user indicates compression, compressed_edges is the list of roots after the compression has taken place
	