# Write a Python function that takes a list and returns a new list with unique elements of the first list


def unique_list(lst:list) -> list:
  return list(set(lst))


print(unique_list([1,1,1,1,2,2,3,3,3,3,4,5]))