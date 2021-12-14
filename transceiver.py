from vars import get_clock_sleep, encode_data_random, encode_data, write_file, data_start_end_key
import multiprocessing
import os
#from gpiozero import LED
#from gpiozero import DigitalOutputDevice
from time import sleep as wait

try:
    os.remove('clock.txt')
except:
    pass

try:
    os.remove('data.txt')
except:
    pass


clock_speed = get_clock_sleep()
#data = str(encode_data())
data = "101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010"

#print(data)


print(clock_speed)

marker, marker_20 = data_start_end_key()


def output_clock():
  #while True:
  min_clock_length = int((int(len(marker)*2) + int(len(data)))/2)
  for _ in range(min_clock_length):
    clock_value = 0
    #print("CLOCK VAL: " + str(clock_value))
    
    # CLOCK GPIO = 0
    write_file('clock', 0)

    wait(clock_speed)
    
    
    clock_value = 1
    #print("CLOCK VAL: " + str(clock_value))

    # CLOCK GPIO = 1
    write_file('clock', 1)

    wait(clock_speed)

clock_multiprocessing = multiprocessing.Process(target=output_clock)

def output_data():
  
  #transmit marker (start)
  for i in marker:
    if i == "0":
      #DATA GPIO = 0
      write_file('data', 0)
      wait(clock_speed)
    elif i == "1":
      #DATA GPIO = 1
      write_file('data', 1)
      wait(clock_speed)
    else:
      raise ValueError('Binary data encoded wrong')

  #transmit data
  for i in data:
    if i == "0":
      #DATA GPIO = 0
      write_file('data', 0)
      wait(clock_speed)
    elif i == "1":
      #DATA GPIO = 1
      write_file('data', 1)
      wait(clock_speed)
    else:
      raise ValueError('Binary data encoded wrong')
  
  #transmit marker (end)
  for i in marker:
    if i == "0":
        #DATA GPIO = 0
        write_file('data', 0)
        wait(clock_speed)
    elif i == "1":
      #DATA GPIO = 1
      write_file('data', 1)
      wait(clock_speed)
    else:
      raise ValueError('Binary data encoded wrong')


      
data_multiprocessing = multiprocessing.Process(target=output_data)

clock_multiprocessing.start()
data_multiprocessing.start()
