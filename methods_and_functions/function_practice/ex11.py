def spy_game(nums):
    '''
    Write a function that takes in a list of integers and returns True if it contains 007 in order.
    '''
    
    bond = [0,0,7,'end']
    for num in nums:
        if num == bond[0]:
          bond.pop(0) # removes the element from the specified index
          
    return len(bond) == 1
        
        
    

print(spy_game([1,2,4,0,0,7,5])) #True
print(spy_game([1,0,2,4,0,5,7])) #True
print(spy_game([1,7,2,0,4,5,0])) #False

