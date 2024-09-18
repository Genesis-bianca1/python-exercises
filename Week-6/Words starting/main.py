# Function to return a list of words from file
def words_starting(file,lower,upper):
  myfile = open(file, 'r')
  
# Collects words starting between 'lower' & 'upper' parameters of 'words_starting'
  list = []
  
# This is the logic to isolate index 0 from every word in file
  for line in myfile:
    words = line.split()
    for word in words:
      first_letter = word[0]
# The word is saved in 'list' if its index 0 is in range between 'lower' and 'upper' parameters
      if lower <= first_letter <= upper:
        list.append(word)
        
  myfile.close()
  return list

if __name__ == "__main__":
# '[0]' to recognise index 0 only, from user input
  lower = str(input('Enter the lower letter: '))[0]
  upper = str(input('Enter the upper letter: '))[0]
# Function call
  letters = words_starting('richmond.txt',lower,upper)
  print('Words in richmond.txt starting with letters: ',letters)