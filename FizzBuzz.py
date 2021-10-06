factors = []

for i in range(1, 101):
    if i % 3 == 0:
        if i % 5 == 0:
            print('FizzBuzz')
        else:
            print('Fizz')
    elif i % 5 == 0:
        print('Buzz')
    else:
        for j in range (2, i+1):
            if i % j == 0:
                factors.append(j)
        if len(factors) > 1 or i == 1:
            print(i)
        else:
            print('Prime!')
    factors = []