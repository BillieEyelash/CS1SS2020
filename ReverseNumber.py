# reverse a number
number = int(input())
checkneg = number
reverse = 0

if checkneg < 0:
    number *= -1

while number > 0:
    digit = number % 10
    number = number // 10
    reverse *= 10
    reverse += digit

if checkneg < 0:
    reverse += -1

print(reverse)
