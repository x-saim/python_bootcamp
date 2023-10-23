def old_macdonald(name: str) -> str:
  
  #name must be 4 letters minimum.
    if len(name) > 3:
        return name[:3].capitalize() + name[3:].capitalize()
    else:
        return 'Name is too short!'
  
print(old_macdonald('macdonald'))
