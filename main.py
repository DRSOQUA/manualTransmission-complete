from time import sleep as wait
from vars import get_clock_sleep
from transceiver import *

print('transmittion started')

print('starting reciever')

offset_time = get_clock_sleep()

wait(offset_time)

print('started')

#input('')

#from experiments import *


from receiver import *

from experiments import *

""" maybe start reciever before the transiver?? """