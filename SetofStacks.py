#!/usr/bin/env python
import math

class SetOfStacks:
  def __init__(self, stack_size):
    self.stack_size = stack_size
    self.container = []
    self.index = 0

  def isEmpty(self):
    return self.index == 0

  def push(self, element):
    self.index += 1
    if len(self.container) < math.ceil(float(self.index) / float(self.stack_size)):
      self.container.append([])
    self.container[-1].append(element)
    print('{} is pushed into the stack'.format(element))

  def top(self):
    return self.container[-1][-1] if not self.isEmpty() else None

  def pop(self):
    if not self.isEmpty():
      self.index -= 1
      element = self.container[-1].pop()
      if len(self.container[-1]) == 0:
        self.container.pop()
      print('{} is popped from the stack'.format(element))
      return element
    else:
      print('Stack is empty')
      return None
        
test = SetOfStacks(3)
test.pop()
test.push('A')
test.push('B')
test.push('C')
test.pop()
test.push('D')
test.push('E')
print(test.top())
test.push('F')
test.push('G')
test.push('H')

print(test.top())
print(test.container)

