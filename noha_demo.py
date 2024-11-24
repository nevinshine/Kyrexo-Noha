# noha_demo.py
print("Welcome to Noha!")
command = input("Describe your task in plain English: ")

if "create a file" in command:
    with open("example.txt", "w") as f:
        f.write("This file was created by Noha.")
    print("File 'example.txt' created successfully.")
else:
    print("Task not recognized. Stay tuned for future updates!")
