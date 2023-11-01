def blackjack(a, b, c):
  '''
  Given three integers between 1 and 11, if their sum is less than or equal to 21, return their sum. If their sum exceeds 21 *and* there's an eleven, reduce the total sum by 10. Finally, if the sum (even after adjustment) exceeds 21, return 'BUST'
  
  '''
  if all(1 <= x <= 11 for x in [a, b, c]):
      total_sum = a + b + c
      if total_sum <= 21:    
        return total_sum
      elif 11 in [a, b, c] and total_sum - 10 <= 21:
        return total_sum - 10
      else:
        return 'BUST'
  else:
    return 'Input values must be between 1 and 11'

print(blackjack(1, 2, 3))  # 6
print(blackjack(9, 9, 9))  # 'BUST'
print(blackjack(9, 11, 9))  # 19