import os



try:
    os.remove("python.txt")
except FileNotFoundError:
    print("File already deleted")