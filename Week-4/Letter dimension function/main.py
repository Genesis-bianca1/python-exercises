def is_letter(weight,length,width,depth):
  measures = [weight,length,width,depth]

  if weight > 100 or depth > 5:
    return False
    
# Lenght and Width Criteria Check
  if not (90 <= length <= 240 and 90 <= width <= 165):
    return False

# Check if at least one dimension >= 140mm, excluding weight(g)
  for measure in measures[1:]: 
    if measure >= 140:
      return True
# Not one dimension >= 140
  return False