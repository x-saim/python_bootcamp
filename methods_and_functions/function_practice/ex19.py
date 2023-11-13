'''

Write a Python function to check whether a string is pangram or not. (Assume string passed in does not have any punctuation)
 

E.g: 'The quick brown fox jumps over the lazy dog'
'''

import string

def ispangram(str1, alphabet=string.ascii_lowercase):
  alphabet_arr = list(alphabet)

  #Handling Edge Cases
  str1 = set(str1.replace(' ', '').lower()) # lowercase, remove spaces, grab unique characters
  
  for char in str1:
    if char in alphabet_arr:
      alphabet_arr.remove(char)
  return len(alphabet_arr) == 0


print(ispangram('The quick brown fox jumps over the lazy dog'))
print(ispangram('Pack my box with five dozen liquor jugs.'))
print(ispangram('The five boxing wizards jump quickly.'))