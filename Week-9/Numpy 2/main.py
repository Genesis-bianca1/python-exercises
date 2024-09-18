import numpy as np


def caesar_2(str,n):
  result = str
  if len(str) == 1:
    uni = ord(str)
    if str >= 'a' and str <='z':
      start = ord('a')
      offset = (n + uni - start)%26
      result = chr(start + offset)
    elif str>= 'A' and str <= 'Z':
      start = ord('A')
      offset = (n + uni - start)%26
      result = chr(start + offset)
  return result

caesar_3 = np.frompyfunc(caesar_2,2,1)

def caesar(arr,n):
  return caesar_3(arr,n)


if __name__ == "__main__":
  myarr = np.array(['V','i','d','i','.',' ','V','i','c','i','!'])
  cypher = caesar(myarr,5)
  print(repr(cypher))