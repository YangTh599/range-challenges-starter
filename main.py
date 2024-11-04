# Thayer Yang  
# 4 NOV 2024
# Range Challenges

# Counting Up & Down

from time import sleep

num = int(input("Enter an integer: "))

for number in range(1, num+1):
    print(number)
    sleep(.25)

print()

print("Now counting down...")
for number in range(num, 0, -1):
    print(number)
    sleep(.25)
print('We have lift off!!')

#Number Cubes
print()    

for number in range(1,11):
    print(f'The cube of {number} is {number**3}')
    sleep(.25)

# Multiplication Table
print()

num = int(input("Enter a number: "))

for number in range(1, num+1):
    print(f'{number} times {num} equals {number*num}')
    sleep(.25)

# List Iteration
    
numbers = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
num_elements = len(numbers)

results = 0
for number in range(num_elements):
    results += numbers[number]
print(f'''Results: {results}
Actual Sum: {sum(numbers)}''')