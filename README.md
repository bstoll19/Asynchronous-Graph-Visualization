# Asynchronous-Graph-Visualization
About graphing.py
===================

graphing.py is an interactive set of graphs (wave, dot, and chip) that continously update the progression of asynchronous computer chips over time.

It requires the input of an activity file in line 12 along with an input of a .prs file in line 191.

It internally uses GraphViz [dot output format](https://www.graphviz.org/doc/info/output.html#d:dot) as an intermediate format and [Python tkinter Tcl/Tk](https://docs.python.org/3/library/tk.html) for rendering. It also uses classes from union_find.py and graphvizlayout.py.

Features
--------

Wave Graph:

- Displays selected nodes, each with a unique color, and their value changes by graphing time (x-axis) and value (y-axis)
- Gives information regarding name and time of node under mouse
- Magnifies nodes clicked on

Dot Graph:

- Displays all nodes and their value changes by graphing time (x-axis) and nodes (y-axis) with colored points to explain the change (0 --> red, 1 --> green)
- Gives information regarding name and time of node under mouse
- Shows a linked path through which the chip travels

Chip Graph:

- Allows for node compression and decompression for ease of viewing
- Shows node value through color (0 --> red, 1 --> green)
- Highlights edges causing change in blue
- Updates time in upper left corner
- Right click on node:
	- if the clicked node is a cluster, it will be decompressed by the entered amount
	- if the clicked node is singular, it will be displayed in another window
	- nodes displayed in purple in later generations are nodes that were not withing the cluster or singular node selected, but do interact with it
- Left click on node:
	- if the clicked node is a cluster, the path of the name of the node will be shown on the wave graph
	- if the clicked node is a singular, the path of that node will be shown on the wave graph
	- if the node is already shown on the wave graph, it will be hidden

Known Issues
------------

- When two nodes from the same root are both extended into their own chip graphs, they do not run simultaneously
- If the aforementioned situation occurs and the running node is exited, the time reverts back to that of the idle node

Screenshots
-----------

- [Compressed Chip Graph](https://github.com/bstoll19/Asynchronous-Graph-Visualization/blob/master/Pictures/Compressed%20Chip%20Graph.png)
- [Dot Graph](https://github.com/bstoll19/Asynchronous-Graph-Visualization/blob/master/Pictures/Dot%20Graph.png)
- [Not Compressed Chip Graph](https://github.com/bstoll19/Asynchronous-Graph-Visualization/blob/master/Pictures/Not%20Compressed%20Chip%20Graph.png)
- [Singular Node Chip Graph](https://github.com/bstoll19/Asynchronous-Graph-Visualization/blob/master/Pictures/Singular%20Node%20Chip%20Graph.png)
- [Wave Graph]()

Requirements
------------

- [Python 3](https://www.python.org/download/)
- [Graphviz](http://www.graphviz.org/Download.php)
- tkinter

License
-------

The project is licensed under the MIT license.
