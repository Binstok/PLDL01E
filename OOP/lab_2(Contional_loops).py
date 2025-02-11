print('1. Implement Conditional Statement')
#input the number
x = int(input('Input a number: '))

#conditional statement
if x > 0:
    print('The number is positive')
elif x < 0:
    print('The number is negative')
else:
    print("The number is Zero")

#loop
print('')
print('2. Use loops to process data')
for i in range(1, 21):
    if i %2 == 0:
        print(i)

while True:
    y = int(input('Input a number (if zero the loop will end): '))
    if y == 0:
        break
    print(f'Entered number: {y}')
print(f'Loop ended, entered number: {y}')

#loop control statement
print('')
print('3. Loop control statements')
for i in range(1, 21):
    if i % 5 == 0:
        continue
    elif i > 15:
        break
    print(i)


