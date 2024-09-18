def is_small_parcel(weight,length,width,depth):
  
  dimensions = length + width + depth

  if weight > 2000:
    return False

  if length > 60 or width > 60 or depth > 60:
    return False
    
  if dimensions > 90:
    return False

  return True