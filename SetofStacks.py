#!/usr/bin/env python3

class SetOfStacks:
    def __init__(self, stack_size):
        self.stack_size = stack_size
        self.subcontainer = []
        self.container = []
        self.slot_index = 0

    def isEmpty(self):
        return self.container == [] and self.subcontainer = []


    def push(self, element):
        print('{} is pushed into the stack'.format(element))
        self.subcontainer.append(element)
        self.slot_index += 1
        if self.slot_index == self.stack_size:
            self.container.append(self.subcontainer)
            self.subcontainer = []
            self.slot_index = 0

    def top(self):
        if self.container == [] and self.subcontainer == []:
            print('Stack is empty')
        elif self.subcontainer == []:
            return self.container[-1][-1]
        else:
            return self.subcontainer[-1]

    def pop(self):
        if self.container == [] and self.subcontainer == []:
            print('Stack is empty')
        elif self.subcontainer == []:
            last_stack = self.container[-1]
            print('{} is popped from the stack'.format(last_stack[-1]))
            self.subcontainer = last_stack[0:-1]
            self.slot_index = self.stack_size - 1
            self.container.pop()
        else:
            self.slot_index -= 1
            print('{} is popped from the stack'.format(self.subcontainer[-1]))
            return self.subcontainer.pop()

    def popAt(self, stack_num):
        pass
        
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
print(test.subcontainer)



