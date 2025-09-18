tokens = []
variables = {}
OPERATORS = ['+', '-', '*', '/', '(', ')', '=']


def tokenize(strippedStuff):
    i = 0
    tokenList = []
    lhsVariable = None
    numBuffer = ""
    for x in strippedStuff:
        if x.isdigit():
            numBuffer += x
        else:
            if numBuffer != "":
                tokenList.append(int(numBuffer))
                numBuffer = ""
            tokenList.append(x)


    if numBuffer != "":
        tokenList.append(int(numBuffer))

    if '=' in tokenList:
        lhsVariable = tokenList[0]
    
    print(tokenList)
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


#Need to add logic to check for parentheses 



    if '=' in tokens:
        rhsTokens = tokens[2:]
        lhsVariable = tokens[0]
    else:
        lhsVariable = None
        rhsTokens = tokens[:]

    i = 1
    while i < len(rhsTokens) -1: #i is the operator, i-1 is the previous number, i+1 is the current nubmber
        if rhsTokens[i] == '*':
            result = rhsTokens[i-1] * rhsTokens[i+1]
            rhsTokens[i-1:i+2] = [result]
        elif rhsTokens[i] == '/':
            result = rhsTokens[i-1]/ rhsTokens[i+1]
            rhsTokens[i-1:i+2] = [result]
        else:
            i+=2
    i = 1
    while i < len(rhsTokens) - 1:
        if rhsTokens[i] == '+':
            result = rhsTokens[i-1] + rhsTokens[i+1]
            rhsTokens[i-1:i+2] = [result]
        elif rhsTokens[i] == '-':
            result = rhsTokens[i-1] - rhsTokens[i+1]
            rhsTokens[i-1:i+2] = [result]
    
    finalValue = rhsTokens[0] #This should be the final value
    print(f'Final value is {finalValue}')

    if lhsVariable:
        variables[lhsVariable] = finalValue
    return finalValue







while True:
    stuff = input("Enter an expression")
    strippedStuff = stuff.replace(" ", "")
    tokens, lhsVariable = tokenize(strippedStuff)

    tokens = variableReplace(tokens, OPERATORS, variables)
    finalValue = evaluate(tokens, variables)
    print(finalValue)
    print(f"Tokens are: {tokens}")
    print(f"Variables are {variables}")



    


