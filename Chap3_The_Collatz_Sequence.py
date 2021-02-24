def collatz(number):
    if number % 2 == 0:
        return number // 2
    else:
        return 3 * number + 1

print('Enter number:')
try:
    while True:
        n = int(input())
        temp = collatz(n)
        print(temp)
        if temp == 1:
            break
except ValueError:
    print('Must enter an intiger')
