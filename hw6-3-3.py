# MEE 11/16/21

list = []

list = [int(numbers) for numbers in input("Enter a list of 5 numbers seperated by spaces: ").split()]

total = int(list[0]) + int(list[1]) + int(list[2]) + int(list[3]) + int(list[4])

print(total)