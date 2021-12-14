from vars import get_clock_sleep, data_start_end_key, all_equal
from time import sleep as wait


clock_speed = get_clock_sleep()

check_speed = clock_speed/2

recieved_data = []

dump_compare = []

i=0
while True:
  i+=1
  with open("clock.txt", 'r') as f:
    for line in f:
      pass
    prev_val = line

  wait(check_speed)

  with open("clock.txt", 'r') as f:
    for line in f:
      pass
    curr_val = line

  dump_compare.append(curr_val)
  foo = dump_compare[-50:]
  foo = [i.replace('\n','') for i in foo]
  foo = list(map(int, foo))
  #print(foo)

  if i>15:
    if all_equal(foo) == True:
      break

  if curr_val > prev_val:
    #print('SWITCHED FROM 0 TO 1')
    with open("data.txt", 'r') as f:
      for line in f:
        pass
      temp_data = line
    
    recieved_data.append(temp_data)

recieved_data = [i.replace('\n','') for i in recieved_data]
recieved_data = ''.join(recieved_data)
print(recieved_data)
