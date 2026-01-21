import os

#write
file = open("users.txt", "w")
file.write("COCACOLA\n")
file.close()


#read
file = open("users.txt", "r")
content = file.read()
print(content)
file.close()


#update
file = open("users.txt", "r")
content = file.read()
print(content)
file.close()

file = open("users.txt", "w")
content = file.write(COCACOLITA\n)
file.close()

#delete
#os.remove("users.txt")