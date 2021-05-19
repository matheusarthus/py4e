def arithmetic_arranger(problems, hasAnswer=False):
    finalLine1 = ''
    finalLine2 = ''
    finalLine3 = ''
    finalLine4 = ''
    count = 0

    if len(problems) > 5:
        return ("Error: Too many problems.")

    for problem in problems:
        splitedProblem = problem.split()
        operand1 = splitedProblem[0]
        operand2 = splitedProblem[2]
        operator = splitedProblem[1]

        if operator != '+' and operator != '-':
            return ("Error: Operator must be '+' or '-'.")
        if len(operand1) > 4 or len(operand2) > 4:
            return ("Error: Numbers cannot be more than four digits.")
        try:
            numberOperand1 = int(operand1)
            numberOperand2 = int(operand2)
        except:
            return ("Error: Numbers must only contain digits.")

        line3 = '--'

        if len(operand1) > len(operand2):
            for i in range(len(operand1) - len(operand2)):
                operand2 = ' ' + operand2
            for i in range(len(operand1)):
                line3 = line3 + '-'
        elif len(operand2) > len(operand1):
            for i in range(len(operand2) - len(operand1)):
                operand1 = ' ' + operand1
            for i in range(len(operand2)):
                line3 = line3 + '-'
        else:
            for i in range(len(operand2)):
                line3 = line3 + '-'

        line1 = '  ' + operand1
        line2 = operator + ' ' + operand2
        line3 = line3

        if count >= 1:
            line1 = '    ' + line1
            line2 = '    ' + line2 
            line3 = '    ' + line3 

        finalLine1 = finalLine1 + line1
        finalLine2 = finalLine2 + line2
        finalLine3 = finalLine3 + line3

        if hasAnswer:
            response = 0

            if operator == '+':
                response = str(numberOperand1 + numberOperand2)
            else:
                response = str(numberOperand1 - numberOperand2)

            for i in range(len(line3) - len(response)):
                response = ' ' + response

            line4 = response

            finalLine4 = finalLine4 + line4

        count += 1

    totalString = finalLine1 + '\n' + finalLine2 + '\n' + finalLine3

    if hasAnswer:
        totalString = totalString + '\n' + finalLine4
    
    return totalString