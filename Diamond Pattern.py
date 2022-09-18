x = int(input("Enter the number of rows: "))
rows = x

# Upper half of the pattern
for i in range(1, rows):
    for j in range(1, rows - i):
        print(' ', end = ' ')
    for j in range(0, 2 * i - 1):
        print('*', end = ' ')
    print()

# Lower half of the pattern
for i in range(rows - 2, 0, -1):
    for j in range(1, rows - i):
        print(' ', end = ' ')
    for j in range(0, 2 * i - 1 ):
        print('*', end = ' ')
    print()
