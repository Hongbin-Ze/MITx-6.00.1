# Problem 3
# (15/15 points)
# Assume s is a string of lower case characters.

# Write a program that prints the longest substring of s in which the letters occur in alphabetical order. 
# For example, if s = 'azcbobobegghakl', then your program should print:
# Longest substring in alphabetical order is: beggh

# In the case of ties, print the first substring. 
# For example, if s = 'abcbcd', then your program should print:
# Longest substring in alphabetical order is: abc

count = 0
maxcount = 0
result = 0

for i in range(len(s)-1):
    if (s[i] <= s[i+1]):
        count += 1
        if count > maxcount:
            maxcount = count
            result = i + 1
    else:
        count = 0
start = result - maxcount
print('Longest substring in alphabetical order is:', s[start:result + 1]) 
