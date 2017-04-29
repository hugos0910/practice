#!/usr/bin/env python3

# Implement a stack
class Stack:
  def __init__(self):
    self.items = []

  def isEmpty(self):
    return self.items == []

  def push(self, item):
    self.items.append(item)

  def pop(self):
    return self.items.pop()

  def peek(self):
    return self.items[len(self.items)-1]

  def size(self):
    return len(self.items)

# 3.2
# Took me 10 min, I've learned this before
num_stack = Stack()
min_stack = Stack()
numbers = [3, 5, 6, 1, 4, 5, 8]

for num in numbers:
  if num_stack.isEmpty() or num < min_stack.peek():
    num_stack.push(num)
    min_stack.push(num)    
  else:
    num_stack.push(num)
    min_stack.push(min_stack.peek())

  print(num_stack.peek(), min_stack.peek())


# Implement a queue using two stacks.  Saw many videos titled this,
# wanted to give it a try myself.

class Queue():
  def __init__(self):
    self.items =[]

  def isEmpty(self): 
    return self.items == []

  def enqueue(self, item):
    self.items.append(item)

  def dequeue(self):
    return self.items.pop()

  def peek(self):
    return self.items[len(self.items)-1]

  def size(self):
    return len(self.items)

# T1B1141707135WKD
# uscis
# 800-375-5283
# 1 2 2 2