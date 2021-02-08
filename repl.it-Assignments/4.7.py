# find the number of zeroes in a list
def find_0(n):
  numOfZeros = 0
  for i in range(n):
    number = int(input())
    if number == 0:
      numOfZeros += 1
    else:
      continue
  return numOfZeros

def run():
  n = int(input())
  print(find_0(n))

def test():
  print(find_0(5) == 2)   # enter 0,700,0,200,2
  print(find_0(0) == 0)
  print(find_0(1) == 0) # enter 1

test()
#run()
