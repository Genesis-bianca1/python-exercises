if __name__ == "__main__":
  # A program to detect overlapping events

  # User input commands for event A and B

  start_hourA = int(input('Enter the start hour of event A:'))
  durationA = int(input('Enter the duration of event A (in hours):'))
  end_hourA = start_hourA + durationA

  start_hourB = int(input('Enter the start hour of event B:'))
  durationB = int(input('Enter the duration of event B (in hours):'))
  end_hourB = start_hourB + durationB

  #Here is the logic to determine the overlapping

  if start_hourB >= end_hourA and end_hourB > start_hourA or start_hourA >= end_hourB and end_hourA > start_hourB:
    print ('Events do not overlap')
  else:
    print('Events overlap')
