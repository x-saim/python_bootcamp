

def master_yoda(sentence: str) -> str:
  
  '''
  Given a sentence, return a sentence with the words reversed.
  master_yoda('I am home') --> 'home am I'
  
  '''
  sent_split = sentence.split(' ')
  
  #Two Pointer Method
  left = 0
  right = len(sent_split) - 1
  
  while (left <= right):
    temp = sent_split[left]
    sent_split[left] = sent_split[right]
    sent_split[right] = temp
    left+=1
    right-=1

  return sent_split

print(master_yoda('I am home'))
print(master_yoda('We are ready'))