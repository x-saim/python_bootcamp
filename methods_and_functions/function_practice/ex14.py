# Write a function that checks whether a number is in a given range (inclusive of high and low)

def ran_check(num, low, high) -> str:
  if num in range(low, high + 1):
    return f'{num} is in the range between {low} and {high}'
  else:
    print('The number is outside the range')

print(ran_check(5,2,7))


def ran_bool(num, low, high) -> bool:
    return num in range(low, high + 1)

print(ran_bool(5,2,7))