# check is a number is a palindrome
def get_int():
    while True:
        try:
            return int(input())
        except:
            continue

def is_palindrome(n):
    if n < 0:
        n *= -1
    n = str(n)

    length = len(n)
    for i in range(length // 2):
         if n[i] != n[length - (i + 1)]:
             return False
    return True

def run():
    n = get_int()
    print(is_palindrome(n))

def test():
    print(is_palindrome(1234) == False)
    print(is_palindrome(1221) == True)
    print(is_palindrome(-1221) == True)
    print(is_palindrome(-1234) == False)
    print(is_palindrome(-12521) == True)
    print(is_palindrome(12521) == True)
    print(is_palindrome(12345) == False)

test()
# run()
