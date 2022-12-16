
# File handling

file = open("file.txt", "r")
print("reading 10 characters :", file.read(10))
# Move the cursor to the first character
file.seek(0)
print(file.read())
file.close()

fa = open("file.txt", "a")
fa.write("\nNow I'm appending this line")
fa.close()
print("\nAfter appending a new line")
fo = open("file.txt", "r")
print(fo.read())
fo.close()

fd = open("file.txt", "w")
fd.seek(0)
fd.write("I'm overriding the content")
fd.close()
fo = open("file.txt", "r")
print("\nAfter override :\n", fo.read())
