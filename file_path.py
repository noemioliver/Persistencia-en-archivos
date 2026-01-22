import os

def write_file(archivo):
    file = open(archivo, "w")
    file.write("INICIO")
    file.close()

def read_file(archivo):
    file = open(archivo, "r")
    print(file.read())
    file.close()

def update_file(archivo):
    file = open(archivo, "w")
    file.write("ACTUALIZADO")
    file.close()

def delete_file(archivo):
    os.remove(archivo)

write_file("users.txt")
read_file("users.txt")
update_file("users.txt")
read_file("users.txt")
# delete_file("users.txt")
