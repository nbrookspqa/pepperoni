def x_to_3(string):
  for i in range(len(string)):
    if string[i] == 'x' or string[i] == 'X':
      string[i] = '3'
  return string
