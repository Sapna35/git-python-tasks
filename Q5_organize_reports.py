import os
import shutil

reports_folder = os.path.join(os.getcwd(), 'reports')

if not os.path.exists(reports_folder):
    os.mkdir(reports_folder)
    print("Created 'reports' folder.")
else:
    print("'reports' folder already exists.")

files = os.listdir()

for file in files:
    if os.path.isfile(file) and file.endswith('.txt'):
        print(f"Found .txt file: {file}")
        shutil.move(file, os.path.join(reports_folder, file))
        print(f"Moved {file} to 'reports' folder.")
