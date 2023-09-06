'''a = input("Enter the number: ")
print(f"Multiplication table of {a} is ")

try:
    for i in range (1, 11):
        print(f"{int(a)} X {i} = {int(a)*i}")
except : # if there is no use to write ( Exception as e) then it can be removed if we are not taking ee as the error
    print("Invalid Input - the entered input should be in numbers")

print("some it lines of code ")
print("End of program")'''

try:
    num = int(input("Enter an integer: "))
    a = [6, 3]
    print9a[num]
except ValueError: #handling value error
    print("Number is not an integer")
#can add multiple error, according to the error that is raised after the enter of the user
except IndexError:
    print("Index Error")

#there can also be a top level obejct erro where we will nor need to add exception for every code but there will be main error object  at the top