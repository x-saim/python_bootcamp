def makes_twenty(int1: int, int2: int) -> bool:
    return int1 == 20 or int2 == 20 or int1 + int2 == 20

print(makes_twenty(20, 10))  # Output: True (int1 is 20)
print(makes_twenty(2, 3))    # Output: False 
