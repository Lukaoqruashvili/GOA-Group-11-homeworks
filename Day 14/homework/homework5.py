name_array = []

age = int(input("Enter your age: "))

if age > 18:
    
    name = input("Enter your name: ")

    name_array.append(name)

    print("name in the array:", name_array)
else:
    print("you arent eligible to provide a name")
