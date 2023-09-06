'''try:
    l = [ 1, 4, 6, 7]
    i = int(input("Enter the index: "))
    print(i)
except:
    print("some error accurred")

finally:
    print(" The finally keyword is always ececuted, no matter  what is the error in the code")'''

# it is mostly usefull when it is used in function as it


#custom error in python
#when you want to throw  any specific error at the specific action by the user
#Can  study error from documentation in error file ( https://docs.python.org/3/library/exceptions.html?highlight=built%20exception#Exception
a = int(input(" Enter any value between 5 and 9"))

if (a <5 or a > 9):
    raise ValueError("value should be between 5 and 9 ")