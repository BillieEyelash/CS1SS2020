# generalize sort in ascending order
def get_list():
    numbers = list()
    while True:
        number = input()
        try:
            number = int(number)
            numbers.append(number)
        except:
            if number == 'done' and len(numbers) >= 1:
                return numbers
    return numbers

def sort(numbers):
    sorted = list()
    while len(numbers) > 0:
        sorted.append(min(numbers))
        numbers.remove(min(numbers))
    return sorted

def run():
    print(sort(get_list()))

def test():
    print(sort([3, 2, 4]) == [2, 3, 4])
    print(sort([0]) == [0])
    print(sort([3]) == [3])
    print(sort([0, -1, 1]) == [-1, 0, 1])

#run()
test()
