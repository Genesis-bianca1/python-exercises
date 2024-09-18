def do_next_op(state,capA,capB):
  a, b = state

  if a == 0:
    state[0] = capA
    return 'FA'
  elif b == capB:
    state[1] = 0
    return 'EB'
  else:
    vol_to_pour = min(a, capB - b)
    state[0] -= vol_to_pour
    state[1] += vol_to_pour
    return 'AB'