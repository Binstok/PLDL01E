print('1. Working with data types')

my_int = 10
my_float = 1.38
my_complex = 9j
my_str = 'Ryley'
my_list = [1, 2, 3, 4, 5]
my_tuple = (1, 2, 3, 4, 5)
my_set = {1, 2, 3, 4, 5}
my_frozenset = frozenset({1, 2, 3, 4, 5})
my_dict = {'Name': 'Ryley', 'Age':19}
my_bool = False
my_none = None

#print data types
print(type(my_int))
print(type(my_float))
print(type(my_complex))
print(type(my_str))
print(type(my_list))
print(type(my_tuple))
print(type(my_set))
print(type(my_frozenset))
print(type(my_dict))
print(type(my_bool))
print(type(my_none))

print('')
print('2. Perform operations on data types')

#input a number
print('Arithmetic operations in int')
x = int(input('Input a number: '))
y = int(input('Input the second number: '))

# perform the operations
add = x + y
subtract = x - y
multiplication = x * y
division = x/y

#print the results
print('Addition: ', add)
print('Subtraction: ', subtract)
print('Multiplication: ', multiplication)
print('Division: ', division)

#input a number
print('')
print('Arithmetic operations in float')
r = float(input('Input a number: '))
t = float(input('Input the second numnber: '))

#perform the operations
add2 = r + t
subtract2 = r - t
multiplication2 = r * t
division2 = r/t

#display the results
print('Addition: %.2f' % add2)
print('Subtraction: %.2f' % subtract2)
print('Multiplication: %.2f' % multiplication2)
print('Division: %.2f' % division2)

print('')
#Input your str, then add up after print the result
str1 = 'Ryley'
str2 = 'Vince'
result = str1 + ' ' + str2
print(result)

#create list
print('')
my_list2 = [1, 2 ,3]

#adding to list
my_list2.append(5)
my_list2.insert(3, 4)
my_list2.extend([6, 7])
#print the new list
print('Results in adding to mylist: ', my_list2)

#removing elements on the list
my_list2.remove(7)
del my_list2[5]
#print
print('Results in removing elements: ', my_list2)

#creating set
my_set2 = {1, 2, 3}

#adding elements to the set
my_set2.add(4)
#print
print('Adding elements to the set', my_set2)

#removing elements to the set
my_set2.remove(1)
#print
print('Removing elements to the set', my_set2)

print('')
#accesing dict to the keys
print('Accessing dictionary using keys')
color = {'1': 'Red', '2': 'Blue', '3': 'Yellow'}
value = color['1']
value2 = color['3']
print(value)
print(value2)

print('')
print('3. Using Operators')

#input two int number
a = int(input('Input first number: '))
b = int(input('Input the second number: '))

#print arithmetic operations
print(f'Sum: {a + b}')
print(f'Subtraction: {a - b}')
print(f'Multiplication: {a * b}')
print(f'Division: {a/b}')
print(f'Modulus: {a % b}')
print(f'Floor division: {a//b}')
print(f'Exponentiation: {a ** b}')

# Comparison operations
print(f"Equal: {a == b}")
print(f"Not Equal: {a != b}")
print(f"Greater Than: {a > b}")
print(f"Less Than: {a < b}")
print(f"First number is Greater Than or Equal: {a >= b}")
print(f"First number is Less Than or Equal: {a <= b}")

# Logical operations
print(f"Logical AND: {a and b}")
print(f"Logical OR: {a or b}")
print(f"Logical NOT (a): {not a}")
print(f"Logical NOT (b): {not b}")

# Bitwise operations
print(f"Bitwise AND: {a & b}")
print(f"Bitwise OR: {a | b}")
print(f"Bitwise XOR: {a ^ b}")
print(f"Bitwise NOT (a): {~a}")
print(f"Bitwise NOT (b): {~b}")
print(f"Bitwise LEFT SHIFT (a): {a << 1}")
print(f"Bitwise LEFT SHIFT (b): {b << 1}")
print(f"Bitwise RIGHT SHIFT (a): {a >> 1}")
print(f"Bitwise RIGHT SHIFT (b): {b >> 1}")