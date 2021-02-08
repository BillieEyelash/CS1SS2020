# find the number of maxima in a list
def get_list():
  numbers = list()
  n = int(input())
  while n != 0:
    numbers.append(n)
    n = int(input())
  return numbers

def number_of_max(sequence):
  maximumCount = sequence.count(max(sequence))
  return maximumCount

def run():
  print(number_of_max(get_list()))

def test():
  print(number_of_max([1, 7, 9]) == 1)
  print(number_of_max([1, 3, 3, 1]) == 2)
  print(number_of_max([1]) == 1)

# test()
run()
