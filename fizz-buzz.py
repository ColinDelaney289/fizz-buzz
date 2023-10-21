# Python Project One
# Question Two - Loop Practice 
# "Fizz Buzz"

counter = 1
while counter <= 100:
    if (counter % 3 == 0) and (counter % 5 == 0):
        print('Fizzbuzz')
    elif counter % 3 == 0:
        print('Fizz')
    elif counter % 5 == 0:
        print('Buzz')
    else:
        print(counter)
    counter += 1