def prodlist(numList):

  if numList == 0:
    return 1
  
  product = 1
  for num in numList:
    product *= num
    
  return product