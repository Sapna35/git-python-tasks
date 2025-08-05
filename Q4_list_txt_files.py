import os

print("Listing .txt files in current directory:")
for file in os.listdir():
    if file.endswith(".txt") and os.path.isfile(file):
        print(file)
