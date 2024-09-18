def main():
    results = read_file('marathon.txt')
    option = ''
    while option != 'Q':
        menu()
        option = input('Select option: ')
        if option == 'S':
            display_competitor(results)
        elif option == 'I':
            display_nbr_in_interval(results)

def read_file(filename):
  myfile = open(filename)
  results = []
  
# Splits the elements separated by comma (of every row)
  for line in myfile:
    element = line.split(',')
    id = element[0]
    time = element[1]
    firstname = element[2]
    lastname = element[3]
# Stores participants' info in separate dictionary sets
    results.append({'id': id, 'time': time, 'firstname': firstname, 'lastname': lastname})
    
  myfile.close()
  return results

def get_interval_data(start_secs, end_secs, results):
  count = 0
  seconds_sum = 0

# Turns participants 'time' to seconds 
# 'time' extracted from dictionary created in read_file() function
  for competitor in results:
    competitor_time = get_secs(competitor['time'])

# Counts participants who finished within the user-specified time range
    if start_secs <= competitor_time <= end_secs:
      count += 1
# Accumlates time to calculate average
      seconds_sum += competitor_time

    if count != 0:
      mean = seconds_sum / count
    else:
      0
  
  return {'count':count, 'mean':mean} 

# FROM USER SELECTING OPTION "S": Input Race_number, SHOWS COMPETITOR'S INFO
def display_competitor(results):
    id_no = input('Enter competitor ID:')
    found = False
    for competitor in results:
        if competitor['id'] == id_no:
            display_competitor_info(competitor)
            found = True
    if not found:
        print('Competitor not found')
    
def display_competitor_info(competitor):
    print('ID :',competitor['id'])
    print('First Name :', competitor['firstname'])
    print('First Name :', competitor['lastname'])

# USER to DEFINE RANGE of TIMES: Shows competitor's STATISTICS WITHIN that SPECIFIED-RANGE
def display_nbr_in_interval(results):
    start_time = input('Enter start time of interval (hh:mm:ss): ')
    start_secs = get_secs(start_time)
    end_time = input('Enter end time of interval (hh:mm:ss): ')
    end_secs = get_secs(end_time)
    interval_data = get_interval_data(start_secs, end_secs, results)
    print('Number of competitors finishing in this interval = ', interval_data['count'])
    if interval_data['count'] != 0:
        secs = interval_data['mean']
        mins = secs//60
        secs = secs%60
        hours = mins//60
        mins = mins%60
        print('Mean time in interval is ',int(hours),'hours',int(mins),'minutes','and ',int(secs),'seconds')
    else:
        print('No competitors in interval')

def get_secs(time):
    time_split = time.split(':')
    seconds = int(time_split[2]) + 60*int(time_split[1]) + 60*60*int(time_split[0])
    return seconds
                      
def menu():
    print('Options are:')
    print('S - Show data for a competitor')
    print('I - Show statistics for competitors finishing in a given interval')
    print('Q - Quit the program')

if __name__ == "__main__":
  main()