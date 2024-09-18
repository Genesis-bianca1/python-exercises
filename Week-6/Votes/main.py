#THIS IS THE FUNCTION YOU NEED TO IMPLEMENT
def head_to_head(canda, candb, filename):
  score = 0
  votes_file = open(filename)
  for vote in votes_file:
    vote_list = vote.split()
    indexa = vote_list.index(canda)
    indexb = vote_list.index(candb)
    if indexa < indexb:
      score += 1
    elif indexa > indexb:
      score -= 1
  votes_file.close()
  return score

#The function below has been put in simply to remind you of the code developed in the lecture.
def lecture_head_to_head(canda, candb,filename):
  score = 0
  votes_file = open('votes.txt')
  for vote in votes_file:
    vote_list = vote.split()
    indexa = vote_list.index(canda)
    indexb = vote_list.index(candb)
    if indexa < indexb:
      score += 1
    elif indexa > indexb:
      score -= 1
  votes_file.close()
  return score

if __name__ == "__main__":
  #THIS CODE IS INTRODUCED PURELY TO SHOW HOW THE FUNCTION head_to_head CAN BE CALLED
  #YOU HAVE TO IMPLEMENT THE FUNCTION head_to_head NOT THE MAIN PROGRAM
  score = head_to_head('Memphis','Knoxville','votes.txt')
  print("Memphis v Knoxville: Score is:",score)