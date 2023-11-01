def paper_doll(text:str) -> str:
    '''
    Given a string, return a string where for every character in the original there are three characters.
    '''
    new_string = ''
    for char in text:
      new_string += char * 3
    
    return new_string
      
    
    


print(paper_doll('Hello'))
print(paper_doll('Mississippi'))