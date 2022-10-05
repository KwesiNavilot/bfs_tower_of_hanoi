# Problem To Solve
The Tower of Hanoi problem is a fun puzzle where the objective is to move an entire stack of blocks from the source position (see initial state) to another position (see goal state).

Three simple rules must be followed:
- Only one block can be moved at a time.
- Each move consists of taking the upper block from one of the stacks and placing it on top of another stack. In other words, a block can only be moved if it is the upper most block on a stack.
- No larger block may be placed on top of a smaller block. In this exercise, the size of a block is indicated by its numeric label.

Assuming that the order of move operators is from Stack1_toStack2, fromStack2_toStack3, fromStack1_toStack3, fromStack3_toStack2, fromStack2_toStack1, fromStack3_toStack1, **write a python script that implements breadth-first search for the given problem.**

Your script should print out if the goal is found and the number of nodes that were expanded to reach the goal. See examples that will be discussed in class for directions.
