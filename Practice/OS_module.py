import os
print(f"Current Working Directory: {os.getcwd()}")

print(os.listdir())

os.chdir("Practice")
print(f"Now your dir is {os.getcwd()}")

os.chdir("..")
print(f"Now Current Working Directory: {os.getcwd()}")