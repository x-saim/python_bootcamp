# Write a python function that accepts a string and calculates the number of upper case letters and lower case letters. 


def up_low(s: str):
  upper_case_count = 0
  lower_case_count = 0
  for char in s:
    if char.isupper():
      upper_case_count += 1
    elif char.islower():
      lower_case_count += 1
    else:
      pass

  return f'No. of Upper case characters : {upper_case_count}\nNo. of Lower case characters : {lower_case_count}'

print(up_low('Hello Mr. Rogers, how are you this fine Tuesday?'))