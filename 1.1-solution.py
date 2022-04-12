def calculations(input):
    stack = []

    for item in input:
        stack.append(item)
    if len(stack) >= 10:
        while len(stack) >= 5:
            for item in stack:
                try:
                    int(item)
                except ValueError:
                    last = stack.pop()
        if last == "." or last == "4" or last == "5" or last == "7":
            return print(("Error 3"))
    else:
        try:
            int(item)
        except ValueError:
            stack.pop()
    print(stack)


ex1 = "2`5@[4.71-*&^%44"
calculations(ex1)
ex2 = "-----------"
calculations(ex2)