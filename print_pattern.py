def print_repeatedly(string, repetitions):
    str = ""
    for x in range(repetitions):
        str = str + string
    print(str)

print_repeatedly("xy", 6)


def print_pattern(string, repetition_list):
    for x in repetition_list:
        print_repeatedly(string, x)


print_pattern("abc", [4, 2, 1])