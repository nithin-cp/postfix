def get_input():
    postexp = raw_input("enter the expression: ")
    return postexp

def push(operand,stack):
    stack.append(int(operand))
    return stack
def eval_post(number2,number1, operator,stack):
    if operator == '+':
        rs = number2 + number1
    elif operator == '*':
        rs =  number2 * number1
    elif operator == '/':
        rs = number2/number1
    elif operator == '-':
        rs = number2 - number1
    return rs
            




