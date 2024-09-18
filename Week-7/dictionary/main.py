def fullpack():
  numbers = {'name':'A','name':'2','name':'3','name':'4','name':'5','name':'6','name':'7','name':'8','name':'9','name':'10','name':'J','name':'Q','name':'K'}
  
  pack = ({'name':'\u2660','name':'\u2665','name': '\u2666','name':'\u2663'})
  
  deck = {}
  
  for each in pack:
    deck ['pack'] = each['name']

  for each in numbers:
    deck['value'] = each['name']

  return deck

