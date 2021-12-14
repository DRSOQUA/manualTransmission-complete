from encdec8b10b import EncDec8B10B

def encode_string (text_to_encode):
  """
  INPUT: string
  OUTPUT: [[character, ascii decimal, ascii binary, [running disparity, encoded]]]

  """


  # string to be transmitted
  sample_string = text_to_encode

  #split the string into a list of characters ('test' = ['t', 'e', 's', 't'])
  list_string = list(sample_string)

  # get ascii decimal representation of each character in list_string
  foo = []
  foo2 = []
  posty = []
  for i in list_string:
    
    text = i
    
    number = ord(text)
    
    if number > 255: #makes sure that this character can be converted to 8b10b (early validation)
      raise ValueError('The ascii character ' + str(i) + ' has no 8b10b equivalent')
    foo.append(number)

    binary = int(format(ord(text), 'b'))
    foo2.append(binary)

    #8b10b encoding
    foo3 = []
    running_disp = 0
    byte_to_enc = number
    running_disp, encoded = EncDec8B10B.enc_8b10b(byte_to_enc, running_disp)
    foo3.append(running_disp)
    foo3.append(encoded)
    posty.append(foo3)




  string_with_decimal = list(map(list, zip(list_string,foo, foo2, posty)))


  
  return string_with_decimal

def get_8b10b_binary(encode_string_list):
  '''
  INPUT: encode_string output
  OUTPUT: cleaned 8b10b binary representation in a list
  '''
  
  foo = []
  for i in encode_string_list:
    
    binary_foo = bin(i[3][1])
    
    if len(binary_foo) == 10:
      binary_foo = binary_foo.replace('0b', '00')
      foo.append(binary_foo)
    
    if len(binary_foo) == 12:
      binary_foo = binary_foo.replace('0b', '')
      foo.append(binary_foo)
    
  return foo


def convert_full_binary(eb10b_binary_output):
  return int(''.join(eb10b_binary_output))


#geazy = encode_string('this is a testing environment')

#print(get_8b10b_binary(geazy))




"""

number = 97
ascii = chr(number)

print(ascii)

text = "a"
number = ord(text)

print(number)
"""