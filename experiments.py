with open("data.txt", "r") as f:
  d = f.readlines()
d = [i.replace('\n','') for i in d]
d = ''.join(d)


with open("clock.txt", "r") as f:
  c = f.readlines()
c = [i.replace('\n','') for i in c]
c = ''.join(c)

