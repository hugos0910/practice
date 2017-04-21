# # 1.1
#20 minutes, I realized this is still cheating afterwards
def unique_char(string):
    c1 = [0]
    empty = False
    string = list(string)
    while len(string) != 0:
        if string[-1] not in string[:-1]: string.pop()
        else: return False
    return True

# I re-did this after 1.3, finished in 5 minutes
def unique_char2(string):
    c = [0]*256
    for i in range(len(string)):
        c[ord(string[i]) - ord('\x00')] += 1
    for i in range(len(c)):
        if c[i] > 1: return False
    return True

print(unique_char2('blah'))
print(unique_char2('hello'))


# # 1.3
# I learned this one before, took me 8 minutes

def is_permutation(string1, string2):
    if len(string1) != len(string2): return False 
    
    c1 = [0]*256
    c2 = [0]*256
    
    for i in range(0,len(string1)):
        c1[ord(string1[i]) - ord('\x00')] += 1
    
    for i in range(0,len(string2)):
        c2[ord(string2[i]) - ord('\x00')] += 1
    
    return c1 == c2
print(is_permutation('ab]c3', ']cba3'))
print(is_permutation('adf', 'cba'))


# # 1.4
# Took me 51 minutes.  I can't think of how to do it without using insert and join since I cannot mute string.
def space_replacement(string):
    c = [0]*len(string)
    for i in range(len(string)):
        c[i] = ord(string[i])
        if c[i] == 32: c[i] = 37
    c_copy = c.copy()
    count = 0
    for i in range(len(c)):
        if c[i] == 37: 
            c_copy.insert(i + count*2 + 1, 50)
            c_copy.insert(i + count*2 + 2, 48)
            count += 1
    char_array = []
    for num in c_copy:
        char_array.append(chr(num))
    return ''.join(char_array)

print(space_replacement('Mr John Smith'))


# # 1.5
# 46 minutes

def compress_string(string):
    new_string = ''
    for pos1 in range(len(string)):
        if pos1 == 0 or string[pos1] != string[pos1-1]:
            count = 1
            pos2 = pos1
            while pos2 < len(string)-1 and string[pos2] == string[pos2+1]:
                count += 1
                pos2 += 1
            new_string += string[pos1] + str(count)
    if len(new_string) >= len(string):
        return string
    else:
        return new_string

print(compress_string('abc[['))
print(compress_string('aabcccccaaa'))

# # 1.7
# Write an algorithm such that if an element in an MxN matrix is 0, its entire row and column are set to 0.

# Took me a little over 20 minutes

mat = [[1,  2,  3,  4,  5],
       [6,  7,  8,  9,  10],
       [11, 12, 13, 14, 15],
       [16, 17, 18, 19, 20],
       [21, 22, 23, 24, 0]]

zero_coord = []
for i in range(len(mat)):
    for j in range(len(mat[i])):
        if mat[i][j] == 0:
            zero_coord.append((i,j))

for i,j in zero_coord:
    mat[i] = 5*[0]
    for k in range(len(mat)):
        mat[k][j] = 0
    
print(zero_coord)
print(mat)


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
    return isSubstring(word1+word1, word2)

print(isSubstring('waterbottle','erbottlewat'))
print(isRotation('waterbottle','erbottlewat'))


