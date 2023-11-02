# FILE IO

file1 = open("priya.txt","wb")
print(file1.mode)
print(file1.name)
file1.write(bytes("this file is originated by me", "UTF-8"))
file1.close()