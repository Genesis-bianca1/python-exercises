# Jug A capacity
# Jug B capacity
# C litres,  C != A and C != B. A,B,&C are integers
# Capacities 

def do_next_op(jugA,jugB):
  # FA - Fill A from tap
  # EB - Empty B
  # AB - Transfer as much from A to B
  
def main(jugA,jugB):
# My code from the previous Jugs problem:
  jugA = 
  jugB = 
  
  if operation == 'FA':
    print(A_capacity,' litres in A and',B_volume,' litres in B')
  elif operation == 'EB':
    print(A_volume,' litres in A and',0,' litres in B')
  elif operation == 'AB':
    new_A_volume = A_volume - min(B_capacity - B_volume, A_volume)
    full_B_jug = B_volume + min(B_capacity - B_volume, A_volume)
    print(new_A_volume,' litres in A and',full_B_jug,' litres in B')
    return operation

