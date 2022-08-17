while True:
    try:
        s = input()
        upper = 0
        lower = 0
        digit = 0
        space = 0

        for i in s:
            if i.isdigit():
                digit += 1
            elif i.isupper():
                upper += 1
            elif i.islower():
                lower += 1
            else: space += 1

        print(lower, upper, digit, space)
    except EOFError:
        break
