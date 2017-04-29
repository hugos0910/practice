#!/usr/bin/env python3
class ThreeStacksFromAnArray:
    def __init__(self, stack_size):
        self.stack_size = stack_size
        self.container = 3 * stack_size * [None]
        self.stack_index = [0, stack_size, 2 * stack_size]

    def isEmpty(self, stack_num):
        for i in range((stack_num - 1) * self.stack_size, stack_num * self.stack_size):
            if self.container[i] != None:
                return False
        return True

    def push(self, stack_num, element):
        stack_index = self.stack_index[stack_num - 1]
        if stack_index < self.stack_size * stack_num: 
            print('{} is pushed into Stack {}'.format(element, stack_num))
            self.container[stack_index] = element
            self.stack_index[stack_num - 1] += 1
            print(self.stack_index)
        else:
            print('Stack {} is full'.format(stack_num))
    def pop(self, stack_num):
        if self.stack_index[stack_num - 1] != self.stack_size * (stack_num - 1): 
            print('{} is popped out of Stack {}'.format(
                self.container[self.stack_index[stack_num - 1] - 1], stack_num)
            )
            self.container[self.stack_index[stack_num - 1] - 1] = None
            self.stack_index[stack_num - 1] -= 1
            print(self.stack_index)
        else:
            print('Stack {} is empty'.format(stack_num))

    def peek(self, stack_num):
        return self.container[self.stack_index[stack_num - 1] - 1]

