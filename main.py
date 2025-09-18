tokens = []
variables = {}
OPERATORS = ['+', '-', '*', '/', '(', ')', '=']


def tokenize(strippedStuff):
    i = 0
    tokenList = []
    lhsVariable = None
    for x in strippedStuff:
        tokenList.append(x)
        try:
            tokenList[i] = int(tokenList[i])
        except:


            print("Not an int") 

        # print(type(tokenList[i]))
        i += 1

    print(tokenList)
    if '=' in tokenList:
        lhsVariable = tokenList[0]
    print(lhsVariable)

    return tokenList, lhsVariable

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
    value = 0
    currentNum = None
    currentOp = None
    if '=' in tokens:
        rhsTokens = tokens[2:]
        lhsVariable = tokens[0]
        value = rhsTokens[0]
        for x in range(1, len(rhsTokens), 2):
            currentOp = rhsTokens[x]
            currentNum = rhsTokens[x+1]
            if currentOp == '+':
                value = value + currentNum
            elif currentOp == '-':
                value = value - currentNum
            elif currentOp == '/':
                value = value/currentNum
            elif currentOp == '*':
                value = value*currentNum
        variables[lhsVariable] = value
        print("updated variable")
    else:
        rhsTokens = tokens[0:]
        value = rhsTokens[0]
        for x in range(1, len(rhsTokens), 2):
            currentOp = rhsTokens[x]
            currentNum = rhsTokens[x+1]
            if currentOp == '+':
                value = value + currentNum
            elif currentOp == '-':
                value = value - currentNum
            elif currentOp == '/':
                value = value/currentNum
            elif currentOp == '*':
                value = value*currentNum

        print(f"Value is {value}")
        
            










while True:
    stuff = input("Enter an expression")
    strippedStuff = stuff.replace(" ", "")
    tokens, lhsVariable = tokenize(strippedStuff)

    tokens = variableReplace(tokens, OPERATORS, variables)
    evaluate(tokens, variables)

    print(f"Tokens are: {tokens}")
    print(f"Variables are {variables}")



    


