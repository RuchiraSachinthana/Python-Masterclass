# rows 5
rows = 5

for i in range(1, rows+1):
    for j in range(0, rows-i+1):
        print(' ', end='')
    # first element should always 1
    one = 1
    for j in range(1, i+1):

        # first value in a line is always 1
        print(' ', one, sep='', end='')

        # using Binomial Coefficient
        one = one * (i - j) // j
    print(" ")