**Description**

A simple 1v1 game played with two virtual hands in a terminal

Main file: /game.py

**Objective** 

Eliminate all of your opponent's "chopsticks"

**How to Play**

Start of game: Each player has 1 chopstick on each hand

During your turn, you can make one of two actions:
- Split: Distribute chopsticks between your hands 
- Hit: Add chopstick count on one of your hands to one of your opponent's hands

If the number of chopsticks on any hand would be >= 5, subtract 5 from that hand 

**Rules to Keep in Mind**
- Can't hit with a hand that has 0 chopsticks
- Can't hit a hand that has 0 chopsticks
- Can't split if the result is the same as before
- You can split such that there is >= 5 chopsticks on a hand, don't forget to subtract 5 (for obvious reasons)


