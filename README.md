TicTacToe with Unbeatable AI in Python.
==============

Callum Ke

This is a command line Player vs AI implementation of TicTacToe written in Python 3.6.
- The AI itself is implemented using a Minimax game tree with Alpha-Beta Pruning.

Inspiration from: https://www.hackerearth.com/blog/developers/minimax-algorithm-alpha-beta-pruning/

How to Run
------------
To run the program you won't need any other libraries. 

	python3.6 TTT.py

How to Play
------------
  To play the game you simply have to run and follow the text based instructions displayed on the terminal.
  
  There are two options: 
  
#  1. AI vs AI
  - This mode functions as a test to demonstrate that the AI works by showing every game ends in a draw. It runs 10000 iterations of the game of the AI playing against itself. The count at the end displays the amount of times either of the AI's won a game, this count should be 0.
  
#  2. AI vs Player
  - The user plays versus the AI as many times as the player wants to. The AI should never lose.
