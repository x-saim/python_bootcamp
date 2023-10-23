def lesser_of_two_evens(a, b):
    # Check if both numbers are even
    if a % 2 == 0 and b % 2 == 0:
        return min(a, b)  # Return the lesser of the two
    else:
        return max(a, b)  # Return the greater of the two

print(lesser_of_two_evens(2, 4))  # Output: 2 (both even, returns the lesser)
print(lesser_of_two_evens(2, 5))  # Output: 5 (one odd, returns the greater)
