# MEE 11/16/21

list1 = []

list1 = [int(numbers) for numbers in input("Enter a list of 5 numbers seperated by spaces: ").split()]

list2 = list1.copy()

list2.sort()

if list2 == list1:
    print("The list is sorted")
else:
    print("The list is not sorted")