
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


def is_small_parcel(weight,length,width,depth):

  dimensions = length + width + depth

  if weight > 2000:
    return False

  if length > 60 or width > 60 or depth > 60:
    return False

  if dimensions > 90:
    return False

  return True

def classify_item(weight,length,width,depth):

# Dimension conversion for is_letter
  mm_length = length * 10
  mm_width = width * 10
  mm_depth = depth * 10

# Call is_letter
  is_letter_mm = is_letter(weight, mm_length, mm_width, mm_depth)

# Call is_small_parcel
  is_small_parcel_ = is_small_parcel(weight,length,width,depth)

# Conditions:
  if is_letter_cm == False and is_small_parcel_ == False:
    return 0
  
  if is_letter_cm == True:
    return 1

  if is_small_parcel_ == True and is_letter_cm == False:
    return 2