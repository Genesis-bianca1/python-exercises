
import random
def countWords(filename):
  myfile = open(filename)
  total = 0
  for line in myfile:
    words = line.split()
    total += len(words)
  myfile.close()
  return total
  
if __name__ == "__main__":
  print("countWords('example.txt') returns ", countWords('example.txt'))
  
if __name__ == "__main__":
  #THIS CODE IS HERE JUST TO ILLUSTRATE HOW THE FUNCTION count_words IS CALLED
  #YOU NEED TO IMPLEMENT THE FUNCTION, NOT THE MAIN PROGRAM
  nbrWords = countWords('example.txt')
  print("Number of words = ",nbrWords)

  countWords.write('_input.txt','w',random.randint())
  countWords = ('_input.txt')
  