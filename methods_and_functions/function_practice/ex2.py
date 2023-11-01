'''
Animal Crackers:

A function that takes a two-word string and returns True if both words begin with the same letter.

'''

def animal_crackers(text:str) -> bool:
  split_text = text.split(' ') #splits words into an array

  return split_text[0][0] != split_text[1][0]


print(animal_crackers('Levelheaded Llama'))
print(animal_crackers('Crazy Kangaroo'))