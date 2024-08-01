# Default directory is root which is opened in vs code
# with open("./day-24-files/my_file.txt") as file:
#     contents = file.read()
#     print(contents)
#     file.close()

with open("./day-24-files/my_file.txt", mode="w") as file:
    file.write("Hey Deshmukh")
