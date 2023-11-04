def summer_69(array):
  '''
  Return the sum of the numbers in the array, except ignore sections of numbers starting with 6 and extending to the next 9 (every 6 will be followed by atleast one 9). Return 0 for no numbers.
  '''
  total = 0
  ignore_nums = False #default 'switch' mode
  
  for num in array:
      if num == 6:
          ignore_nums = True #switch 'on'
      elif num == 9:
          ignore_nums = False #switched 'off
      elif not ignore_nums:
        total += num
  return total

print(summer_69([1, 3, 5])) #--> 9
print(summer_69([4, 5, 6, 7, 8, 9])) #-> 9
print(summer_69([2, 1, 6, 9, 11])) #--> 14