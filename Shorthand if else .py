'''a = 330
b = 3303
print("A") if a > b else print("=")if a == b else print("B")'''

# it is basically, if else in one line, and not in tabluar form
|

#Enumerate function in python
# example( it is a built in function that allows you to loop over a sequence ( lizt tuple, string)
# and get the index and value of sequence  at the same time.


marks = [ 1, 4,57, 89, 45, 12, 67 ]
for index, mark in enumerate(marks):
    print(mark)
    if(index == 3):
        print("harry, awesome!")