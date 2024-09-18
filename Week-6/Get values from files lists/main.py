def get_candidates(filename):
  myfile = open(filename, 'r')
  first_line = myfile.readline()[1:]
  myfile.close()
  
  if first_line:
    candidate = first_line.strip().split()
    return candidate
  else:
    print('File is empty')
    return None

# THIS CODE IS ADDED PURELY TO ILLUSTRATE HOW THE FUNCTION get_candidates WOULD BE CALLED
if __name__ == "__main__":
  cands = get_candidates('votes.txt')
  print("Candidates found in votes.txt:", cands)