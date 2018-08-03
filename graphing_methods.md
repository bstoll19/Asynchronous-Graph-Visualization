graphing.py Methods
=====================

initialize_colors
-----------------

- opens the inputted activity file (line 13)
- sets index to the first line after the initialized reset cycle
- for each line within the initialized reset cycle:
	- randomly generated colored line added to wave graph at specified height according to value
	- binds hover, hover leave, and click methods to added line
	- stores line in wc_items
	- stores coordinates of line in wc_coords
	- if a node is not purple (part of the parent cluster), it's initialized to the color indicated in the activity file

read_data
---------

- runs initialize_colors (shown above)
- creates data list that stores all of the nodes changing at a given time interval (index = time interval)
- runs change_colors

change_colors
-------------

- goes through data (from read_data) line by line and:
	- recursively updates all edges back to their standard state
	- adds to self.time
	- runs change for given line of data
	
change
------

- if it is the first generation:
	- initialize wc_bool to the size of wc_coords and all false
	- adds proper dots to the dot graph in respective colors
	- binds dot graph additions to hover and hover leave
	- updates wc_coords so that the line will change to the other value
	- marks changed lines as true in wc_bool
	- adds points to extend all lines marked as false in wc_bool
	- adjusts scroll on wc and dc canvases to show most recent changes
	- moves 'Current Position' labels to stay centered on screen
- if later generation:
	- recursively calls change on parent graphing instance
- for all generations:
	- updates time label in chip graph
	- if nodes are not purple, changes to indicated color
	- highlights in blue and bolds all edges where change occurs
	
get_eg_parameters
-----------------

- takes information from parent generation and stores into child generation

hover / wc_hover
-----------------

- binds lines (if wc_hover) or dots (if hover) so that the 'Current Position' label will show the name of the node and the time at which the mouse is

hover_leave / wc_hover_leave
----------------------------

- binds lines (if wc_hover_leave) or dots (if hover_leave) so that the 'Current Position' label will return to empty when the mouse leaves a widget

click
-----

- if the line clicked is bolded, it unbolds it
- if the line clicked is unbolded, it bolds it

main
----

- opens prs file and initializes either a graph (if first generation) or an extended_graph (if later generation)
- creates new Tk instance (root)
- if first gen:
	- creates wave graph and dot graph / adds axises and labels
	- names Tk instance 'Chip Graph'
- if later gen:
	- names Tk instance after parent node
- gets dot file (from graphvizlayout)
- click method:
	- binds each node in self.items to click
	- when a label or node is clicked, that node / cluster will be displayed in a new window by creating a new instance of graphing
- left_click method:
	- recursively finds the first gen instance of graphing
	- shows the line of the clicked node / node label on the wave graph
- reads through lines of dot file and calls drw_edge or drw_node as necessary
- adds time label to chip graph
- calls read_data

drw_node
--------

- reads through given line of dot file and:
	- stores color
	- stores coordinates while halving for size
	- creates oval on Chip Graph with given coordinates and color / stores in items
	- creates node label on top of oval with name / stores in items

drw_edge
--------

- reads through given line of dot file and:
	- stores list of points along line
	- halves each point
	- accounts for node height and x offset
	- creates line on Chip Graph with given specifications / stores in items
	- creates edge label if SHOW_EDGE_LBL is true

graphing.py Important Variables / Lists
=========================================

 - index
	- set to the first line from activity that is not part of the initialized reset cycle
- wc_items
	- accounts for everything added to the wc_root canvas
	- the name of a widget in the canvas (to be used in any methods changing the widgets) is one greater than its index in wc_items
- wc_coords
	- records the point lists of each line in the wc_root canvas
	- the index of a given line's point list is 6 less than the index of that line in self.wc_items
- wc_bool
	- tracks which node's line has been updated already in change, so the rest can be updated at the end of the loop
	- the indeces match that of wc_coords
- dc_items
	- accounts for everythin added to the dc_root canvas
	- the name of a widget in the canvas (to be used in any methods changing the widgets) is one greater than its index in dc_items
- time
	- keeps track of the time index that is currently being read (the displayed time in the chip graph is this index * 10)
- items
	- records all the widget's placed on the chip graph canvas
	- the name of the widget in the canvas (to be used in any methods changing the widgets) is one greater than it's index in items
- SHOW_EDGE_LBL
	- allows user to display or hide edge labels given in the graphvizlayout
- graph
	- the first generation instance from graphvizlayout (always needed to find root of names read with graph's union_find)
- current_graph
	- the current generation instance from graphvizlayout (always needed to find root of names read with current_graph's compressionu)

