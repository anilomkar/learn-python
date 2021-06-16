import random
names = ["Anil", "Aditi", "Akhil"]
names.sort()

for name in names:
    print(name)

randomName = random.choice(names)
print(randomName)

numbers = [1,2,3,4,5,6,7,8]
sumOfNumbers = sum(numbers)

print("Sum=" + str(sumOfNumbers))

# name = ""
# while name != "quit":
#     name = input("Enter name to check in list\n")
#     if name != "quit" and name in names:
#         print(name + " is available in list")
#     else:
#         print(name + " is not available in list")
