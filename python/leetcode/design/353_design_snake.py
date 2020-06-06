"""
353. Design Snake Game (Medium)

Design a Snake game that is played on a device with screen size = width x height. Play the game online if you are not familiar with the game.

The snake is initially positioned at the top left corner (0,0) with length = 1 unit.

You are given a list of food's positions in row-column order. When a snake eats the food, its length and the game's score both increase by 1.

Each food appears one by one on the screen. For example, the second food will not appear until the first food was eaten by the snake.

When a food does appear on the screen, it is guaranteed that it will not appear on a block occupied by the snake.

Example:

Given width = 3, height = 2, and food = [[1,2],[0,1]].

Snake snake = new Snake(width, height, food);

Initially the snake appears at position (0,0) and the food at (1,2).

|S| | |
| | |F|

snake.move("R"); -> Returns 0

| |S| |
| | |F|

snake.move("D"); -> Returns 0

| | | |
| |S|F|

snake.move("R"); -> Returns 1 (Snake eats the first food and right after that, the second food appears at (0,1) )

| |F| |
| |S|S|

snake.move("U"); -> Returns 1

| |F|S|
| | |S|

snake.move("L"); -> Returns 2 (Snake eats the second food)

| |S|S|
| | |S|

snake.move("U"); -> Returns -1 (Game over because snake collides with border)
"""

from collections import deque

class SnakeGame(object):
  def __init__(self, width, height, food):
    """
    Initialize your data structure here.
    @param width - screen width
    @param height - screen height 
    @param food - A list of food positions
    E.g food = [[1,1], [1,0]] means the first food is positioned at [1,1], the second is at [1,0].
    :type width: int
    :type height: int
    :type food: List[List[int]]
    """
    self.width = width
    self.height = height
    self.food = deque()
    for food_ in food:
      i, j = food_
      self.food.append((i, j))
    self.pos = deque()
    self.pos.append((0, 0))
    self.pos_set = set()
    self.pos_set.add((0, 0)) 
    self.accu = 0

  def move(self, direction):
    """
    Moves the snake.
    @param direction - 'U' = Up, 'L' = Left, 'R' = Right, 'D' = Down 
    @return The game's score after the move. Return -1 if game over. 
    Game over when snake crosses the screen boundary or bites its body.
    :type direction: str
    :rtype: int
    """
    print 'before', self.pos, self.pos_set, self.accu, self.food
    if direction == "U":
      ii, jj = self.pos[-1]
      # collide with boundary
      if ii == 0:
        return -1
      # eat food 
      elif len(self.food) != 0 and self.food[0][0] == ii-1 and self.food[0][1] == jj:
        self.pos.append((ii-1, jj))
        self.pos_set.add((ii-1, jj))
        self.food.popleft()
        self.accu += 1
      else:
        ix, jx = self.pos.popleft()
        self.pos_set.remove((ix, jx))
        # collide with self
        if (ii-1, jj) in self.pos_set:
          return -1
        self.pos.append((ii-1, jj))
        self.pos_set.add((ii-1, jj))
    elif direction == "D":
      ii, jj = self.pos[-1]
      # collide with boundary
      if ii == self.height-1:
        return -1
      # eat food 
      elif len(self.food) != 0 and self.food[0][0] == ii+1 and self.food[0][1] == jj:
        self.pos.append((ii+1, jj))
        self.pos_set.add((ii+1, jj))
        self.food.popleft()
        self.accu += 1
      else:
        ix, jx = self.pos.popleft()
        self.pos_set.remove((ix, jx))
        # collide with self
        if (ii+1, jj) in self.pos_set:
          return -1
        self.pos.append((ii+1, jj))
        self.pos_set.add((ii+1, jj))
    elif direction == "L":
      ii, jj = self.pos[-1]
      # collide with boundary
      if jj == 0:
        return -1
      # eat food 
      elif len(self.food) != 0 and self.food[0][0] == ii and self.food[0][1] == jj-1:
        self.pos.append((ii, jj-1))
        self.pos_set.add((ii, jj-1))
        self.food.popleft()
        self.accu += 1
      else:
        ix, jx = self.pos.popleft()
        self.pos_set.remove((ix, jx))
        # collide with self
        if (ii, jj-1) in self.pos_set:
          return -1
        self.pos.append((ii, jj-1))
        self.pos_set.add((ii, jj-1))
    else: # direction == "R"
      ii, jj = self.pos[-1]
      # collide with boundary
      if jj == self.width - 1:
        return -1
      # eat food 
      elif len(self.food) != 0 and self.food[0][0] == ii and self.food[0][1] == jj+1:
        self.pos.append((ii, jj+1))
        self.pos_set.add((ii, jj+1))
        self.food.popleft()
        self.accu += 1
      else:
        ix, jx = self.pos.popleft()
        self.pos_set.remove((ix, jx))
        # collide with self
        if (ii, jj+1) in self.pos_set:
          return -1
        self.pos.append((ii, jj+1))
        self.pos_set.add((ii, jj+1))
    print 'after', self.pos, self.pos_set, self.accu, self.food
    return self.accu

# Your SnakeGame object will be instantiated and called as such:
# obj = SnakeGame(width, height, food)
# param_1 = obj.move(direction)
if __name__ == "__main__":
  snake = SnakeGame(3, 2, [[1,2],[0,1]])
  print snake.move("R")
  print snake.move("D")
  print snake.move("R")
  print snake.move("U")
  print snake.move("L")
  print snake.move("U")
