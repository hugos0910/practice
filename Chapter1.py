# # 1.1
# I re-did this after 1.3, finished in 5 minutes
def unique_char2(string):
  ascii_characters = 256
  cs = [0] * ascii_characters
  for c in string:
      cs[ord(c) - ord('\x00')] += 1
  for i in range(ascii_characters):
      if cs[i] > 1: return False
  return True

  d = {}
  for c in string:
    if c in d: return False
    else: d[c] = 1
  return True

print(unique_char2('blah'))
print(unique_char2('hello'))


# # 1.3
# I learned this one before, took me 8 minutes
def is_permutation(string1, string2):
    if len(string1) != len(string2): return False 
    
    c1 = [0] * 256
    c2 = [0] * 256
    
    for c in string1:
        c1[ord(c) - ord('\x00')] += 1

    for c in string2:
        c2[ord(c) - ord('\x00')] += 1
    
    return c1 == c2
  
print(is_permutation('ab]c3', ']cba3'))
print(is_permutation('adf', 'cba'))


# # 1.4
# Took me 51 minutes.  I can't think of how to do it without using insert and join since I cannot mute string.
def space_replacement(string):
  new_string = ''
  for c in string:
    val = '%20' if c == ' ' else c
    new_string += val
  return new_string

  return ''.join(['%20' if c == ' ' else c for c in string])

print(space_replacement('Mr John Smith'))

# # 1.5
# 46 minutes

def compress_string(string):
  new_string = ''
  for pos1 in range(len(string)):
    if pos1 == 0 or string[pos1] != string[pos1-1]:
      count = 1
      pos2 = pos1
      while pos2 < len(string)-1 and string[pos2] == string[pos2 + 1]:
        count += 1
        pos2 += 1
      new_string += string[pos1] + str(count)
  return string if len(new_string) >= len(string) else new_string

print(compress_string('abcs[[')) # -> abcs[[
print(compress_string('aabcccccaaa')) # -> 'a2b1c5a3'

# # 1.7
# Write an algorithm such that if an element in an MxN matrix is 0, its entire row and column are set to 0.

# Took me a little over 20 minutes
def setZero(matrixrix):
  matrix = [[1,  2,  3,  4,  5],
         [6,  7,  8,  9,  10],
         [11, 12, 13, 14, 15],
         [16, 17, 18, 19, 20],
         [21, 22, 23, 24, 0]]
  zero_coord = []
  for i in range(len(matrix)):
      for j in range(len(matrix[i])):
          if matrix[i][j] == 0:
              zero_coord.append((i,j))

  for i, j in zero_coord:
      matrix[i] = len(matrix[i]5) * [0]
      for k in range(len(matrix)):
          matrix[k][j] = 0
    
print(zero_coord)
print(matrix)


# In[ ]:

# # 1.8

# In[138]:

# Assume you have a method isSubstring which checks if one word is substring of another.  
# Given two strings, s1 and s2, write code to check if s2 is a rotation of s1 using only ONE call to isSubstring.
# (e. g. "waterbottle" is a rotation of "erbottlewat")

# I did not get this one, looked at the solution

def isSubstring(word1, word2):
    return word2 in word1

def isRotation(word1, word2):
    return isSubstring(word1 + word1, word2)

print(isSubstring('waterbottle','erbottlewat'))
print(isRotation('waterbottle','erbottlewat')) -> True

