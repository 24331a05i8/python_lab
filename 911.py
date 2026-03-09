# Writing into file
f = open("sample.txt", "w")
f.write("Hello Python\n")
f.writelines(["Line 1\n", "Line 2\n", "Line 3\n"])
f.close()

# Reading file using read()
f = open("sample.txt", "r")
print("Using read():")
print(f.read())
f.close()

# Reading file using readline()
f = open("sample.txt", "r")
print("Using readline():")
print(f.readline())
f.close()

# Reading file using readlines()
f = open("sample.txt", "r")
print("Using readlines():")
print(f.readlines())
f.close()
