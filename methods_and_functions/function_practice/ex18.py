# Write a Python function that checks whether a word or phrase is a palindrome or not.


# Function which return reverse of a string
def palindrome_1(s):
  s = s.replace(' ', '')
  return s == s[::-1]


# Two pointer method implementation

def palindrome_2(s):
  s = s.replace(' ', '')
  l = 0
  r = len(s) - 1
  
  while l < r:
    if s[l] != s[r]:
      return False
    else:
      l += 1
      r -= 1
  return True

print(palindrome_1('helleh'))
print(palindrome_2('helleh'))
print(palindrome_2('madam'))
print(palindrome_2('kayak'))