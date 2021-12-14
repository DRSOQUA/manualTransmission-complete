from encoder import encode_string, get_8b10b_binary, convert_full_binary
from time import sleep
import string
import random
from itertools import groupby


#encoded_data = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(10000))
#encoded_data = '10101010101010'*10
#encoded_data = convert_full_binary(get_8b10b_binary(encode_string(encoded_data)))

def get_clock_sleep(clock_speed = 0.5):
  return clock_speed

def all_equal(iterable):
    g = groupby(iterable)
    return next(g, True) and not next(g, False)

def data_start_end_key(key='11111111111111110'):
  
  # validation
  b = '10'
  count = 0
  for char in key:
    if char not in b:
        count = 1
        break
    else:
        pass
  if count:
    raise ValueError("KEY is not a binary string")

  last_20 = key[-20:]

  return key, last_20

def encode_data_random(string_length=1000):
  encoded_data = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(string_length))
  encoded_data = convert_full_binary(get_8b10b_binary(encode_string(encoded_data)))
  return encoded_data

def encode_data(string_to_encode="test string"):
  encoded_data = string_to_encode
  encoded_data = convert_full_binary(get_8b10b_binary(encode_string(encoded_data)))
  return encoded_data

def write_file(file, content):
  filename = file+".txt"
  with open(filename, "a") as f:
    f.write(str(content)+"\n")

