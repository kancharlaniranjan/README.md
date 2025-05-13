#Read a File and Handling Errors
try:
    file1 = open("Sample.txt", 'r')
    Read_file = file1.read()
    print(Read_file)
    file1.close()
except FileNotFoundError:
    print("Error: The file 'Sample.txt' is not found")

