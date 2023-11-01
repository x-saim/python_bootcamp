def has_33(nums):
    '''
    Given a list of ints, return True if the array contains a 3 next to a 3 somewhere.
    '''
    for index, num in enumerate(nums):
        if num == 3 and index < len(nums) - 1 and nums[index + 1] == 3:
            return True
    return False

print(has_33([1, 3, 3]))  # True
print(has_33([1, 3, 1, 3]))  # False
print(has_33([3, 1, 3]))  # False
