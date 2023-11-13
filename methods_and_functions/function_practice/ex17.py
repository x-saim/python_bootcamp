# Write a Python function to multiply all the numbers in a list


def multiply(numbers: list) -> list:
  product = 1
  
  for num in numbers:
    product *= num
    
  return product


print(multiply([1,2,3,-4]))