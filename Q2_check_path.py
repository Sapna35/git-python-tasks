import os

path = input("Enter a path: ")

if os.path.isdir(path):
    print("It is a directory.")
elif os.path.isfile(path):
    print("It is a file.")
else:
    print("It is neither a file nor a directory.")
