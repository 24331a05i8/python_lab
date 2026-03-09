f = open("file.txt", "w+")

f.write("Python File Handling Example")
f.flush()

print("File pointer position after writing:", f.tell())

f.seek(0)

print("Reading after seek:")
print(f.read())

print("Current position:", f.tell())

f.close()

