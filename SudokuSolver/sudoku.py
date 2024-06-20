import datetime
import numpy as np
import array as arr

def init_sudoku(size):
  matix = np.zeros((size,size), dtype=int)
  return matix

def subcell(x, y, matix):
  temp = []
  for i in range(3):
    now = datetime.datetime.now()
    tmstr = now.strftime('%H%M%S%f')
    time = int(tmstr)
    time = time * time
    print(time)
    for j in range(3):
      if ((time + j ) % 2 == 0):
        if((time%10) < 8):
          temp_value = (time%10 + j)
          if temp_value in temp:
            break
          else:
            temp.append(temp_value)
            matix[x+i][y+j] = temp_value
        else:
          temp_value = (time%10 - j)
          if temp_value in temp:
            break
          else:
            temp.append(temp_value)
            matix[x+i][y+j] = temp_value
      elif ((time + j) % 3 == 0):
        if((time%10) < 8):
          temp_value = (time%10 + j)
          if temp_value in temp:
            break
          else:
            temp.append(temp_value)
            matix[x+i][y+j] = temp_value
        else:
          temp_value = (time%10 - j)
          if temp_value in temp:
            break
          else:
            temp.append(temp_value)
            matix[x+i][y+j] = temp_value
  return matix

def check(matrix, size):
  for i in range(size):
    temp = []
    for j in range(size):
      temp_value = matrix[i][j]
      if temp_value in temp:
        matrix[i][j] = 0
      else:
        temp.append(temp_value)
  for i in range(size):
    temp = []
    for j in range(size):
      temp_value = matrix[j][i]
      if temp_value in temp:
        matrix[j][i] = 0
      else:
        temp.append(temp_value)
  return matrix

def generate(size):
  init_m = init_sudoku(size)
  for i in range(0, size, 3):
    for j in range(0, size, 3):
      print("j: ",j)
      if(j==size):
        break
      else:
        subcell(i,j, init_m)
    if(i==size):
      break
  check(init_m, size)
  return init_m

x = generate(9)
print(x)