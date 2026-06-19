count = 0
total = 0

while True:
    number = int(input('Enter a value (999 stops the program): '))

    if number == 999:
        break

    count += 1
    total += number

print(f'You entered {count} numbers and their sum is {total}!')
