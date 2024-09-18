# Function that returns preferred candidates, called in 'plurality_winner' function.
def count_votes(filename,candidate):
  score = 0
  votes_file = open(filename, 'r')
 
  # Logic to isolate element 1 (most preferred) candidate in 'votes.txt'
  for vote in votes_file:
    preference = vote.split()[1]
    # Checks if most preferred candidate = specified candidate
    if preference == candidate:
      score += 1
      
  votes_file.close()
  return score

# Function that returns the elections winners and their maximum scores only
def plurality_winner(filename,candidates):
  winner_list = []
  # Loop to count votes
  for candi in candidates:
    winner_list.append(count_votes(filename,candi))
  # Identify maximum score among all candidates
  max_score = max(winner_list)
  # Returns winner identity and its max score
  return [candidates[winner_list.index(max_score)],max_score]
  
if __name__ == "__main__":  

  win = plurality_winner('votes.txt',['Memphis','Nashville','Chattanooga','Knoxville'])
  print('Plurality winner from votes.txt is ',win)

  winner = plurality_winner('votes2.txt',['Arthur','Betty','Clare'])
  print('The winner from votes2.txt is ',winner)