# MEE 11/16/21

list1 = input("Input any list of numbers or letters seperated by spaces n")

question = str.lower(input("Do you want to find the middle or the end? "))

list2 = list1.split()
length = len(list2)

if question == "middle":
    print(list2[1:length - 1])
elif question == "end":
    print(list2[:1] + list2[length - 1:])