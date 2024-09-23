# Boardgame Engine
Boardgame engine allowing for implementing any game using scripting language.
The language allows for adding game components, describing their looks, behaviour and position on board.
To implement a game one must describe its components, rules, winning conditions and setup.
The game can be divided into various phases, turns, stages, etc.
Using the provided rules, all player moves will have enforced correctness and automatic counting and housekeeping activities.
In the future it would be possible to provide some "evaluation function" to implement automated players.

## Syntax example

```
Game tic-tac-toe
Players: 2

Marker sign:
  shape: square
  variants: x, o

x:
  text: "X"
o:
  text: "O"

Place main_board:
  ortho_grid 3x3

Action sign.place:
  Player.resources -> main_board.empty_field

Rule winning_rule:
  check each (main_board: row and column and diagonal):
    each sign is uniform
  
Setup:
 9 x -> Player1.resources
 9 o -> Player2.resources
 (choose Player).play
 
Turn:
  sign.place
  if(winning_rule):
    CurrentPlayer wins
    end Game
  else:
    (next Player).play
```

## Warning
All the work is in progress, the above sytax is not-yet-implemented
