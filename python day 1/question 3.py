def case_count(str):
    lst = list(str)
    U = 0
    L = 0
    for i in lst:
        if i.isupper():
            U += 1
        elif  i.islower():
            L += 1
    print("'Uppercase:{}', 'Lowercase:{}'".format(U, L))

case_count("Hello World")
