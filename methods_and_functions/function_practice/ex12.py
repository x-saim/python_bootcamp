def count_primes(num):
  '''
  Write a function that returns the number of prime numbers that exist up to and including a given number
  '''
  
  #check for 0 or 1 input
  if num < 2:
    return 0
  
  #Storing our prime numbers
  primes = [2] 
  x = 3
  
  #x is going through every number up to input num
  while x <= num:
    print(x)
    
    #check if x is prime
    for y in range(3, x, 2):
      if x%y == 0:
        x += 2
        break
    else:
      primes.append(x)
      x += 2
  print(primes)
  return len(primes)

print(count_primes(100))