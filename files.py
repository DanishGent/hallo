mydata = ["this is,\n", "kalto he is.\n", "43 in age.\n"]
myfile = "../data/input01.txt"

with open(myfile, "w") as file:
    file.writelines(mydata)

line_number = 0
with open(myfile) as file:
    for line in file:
        line_number += 1
        print(line.strip())
    print()