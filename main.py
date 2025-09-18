tokens = []
variables = {}
OPERATORS = ['+', '-', '*', '/', '(', ')', '=']
i = 0


while True:
    stuff = input("Enter an expression")
    strippedStuff = stuff.replace(" ", "")

    for x in strippedStuff:
        tokens.append(x)
        try:
            tokens[i] = int(tokens[i])
        except:
            if i == 0:
                variables.update({tokens[i]: 0})  # this is probably sketchy
            elif tokens[i] not in OPERATORS:
                temp = tokens[i]
                tokens[i] = variables[temp]

            print("Not an int")

        print(type(tokens[i]))
        i += 1
