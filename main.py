tokens = []
variables = {}
OPERATORS = ['+', '-', '*', '/', '(', ')', '=']


def tokenize(strippedStuff):
    i = 0
    tokenList = []
    lhsVariable = None
    numBuffer = ""

    for i, x in enumerate(strippedStuff):
        if x.isdigit():
            numBuffer += x
        # This is where I'm checking for a negative number
        elif x == '-':
            if (i == 0 or strippedStuff[i-1] in OPERATORS and strippedStuff[i-1] != ')'):
                numBuffer += '-'  # start the negative number

            else:
                if numBuffer != "":
                    tokenList.append(int(numBuffer))
                    numBuffer = ""
                tokenList.append(x)

        else:
            if numBuffer != "":
                tokenList.append(int(numBuffer))
                numBuffer = ""
            tokenList.append(x)

    if numBuffer != "":
        tokenList.append(int(numBuffer))

    if '=' in tokenList:
        lhsVariable = tokenList[0]

    return tokenList, lhsVariable


def normalize(tokens):
    i = 0
    while i < len(tokens) - 1:
        if tokens[i] == '-' and tokens[i+1] == '-':
            tokens[i:i+2] = ['+']
        elif tokens[i] == '+' and tokens[i+1] == '+':
            tokens[i:i+2] = ['+']
        elif tokens[i] == '+' and tokens[i+1] == '-':
            tokens[i:i+2] = ['-']
        elif tokens[i] == '-' and tokens[i+1] == '+':
            tokens[i:i+2] = ['-']
        else:
            i += 1

    return tokens


def variableReplace(tokens, operators, variables):
    if '=' in tokens:
        lhsIndex = 0
    else:
        lhsIndex = -1
    for x, token in enumerate(tokens):
        if x == lhsIndex:
            continue
        if token not in operators:
            if token in variables:
                tokens[x] = variables[token]

    return tokens


def evaluate(tokens, variables):

    if '=' in tokens:
        rhsTokens = tokens[2:]
        lhsVariable = tokens[0]
    else:
        lhsVariable = None
        rhsTokens = tokens[:]

    while '(' in rhsTokens:
        openParent = None
        for i, token in enumerate(rhsTokens):
            if token == '(':
                openParent = i
            elif token == ')' and openParent is not None:
                closedParent = i

                innerTokens = rhsTokens[openParent+1:closedParent]
                innerResult = evaluate(innerTokens, variables)
                rhsTokens[openParent:closedParent+1] = [innerResult]
                break



    # i is the operator, i-1 is the previous number, i+1 is the current nubmber
    i = 1
    while i < len(rhsTokens) - 1:
        if rhsTokens[i] == '+':
            result = rhsTokens[i-1] + rhsTokens[i+1]
            rhsTokens[i-1:i+2] = [result]
        elif rhsTokens[i] == '-':
            result = rhsTokens[i-1] - rhsTokens[i+1]
            rhsTokens[i-1:i+2] = [result]

    finalValue = rhsTokens[0]  # This should be the final value


    if lhsVariable:
        variables[lhsVariable] = finalValue
    # else:
    #     if type(finalValue) == int and len(rhsTokens) == 1:
    #         print(finalValue)

    return finalValue


while True:
    stuff = input("")
    strippedStuff = stuff.replace(" ", "")

    if strippedStuff == '':
        print("")
        continue

    tokens, lhsVariable = tokenize(strippedStuff)
    tokens = normalize(tokens)
    tokens = variableReplace(tokens, OPERATORS, variables)
    finalValue = evaluate(tokens, variables)

    if '=' in tokens:
        continue

    elif len(tokens) == 1 and type(tokens[0]) is int and tokens[0] in variables:
        print(variables[tokens[0]])
    else:
        print(finalValue)




