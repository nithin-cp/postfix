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
            
def main():
    stack = []
    exp = get_input()
    operators = ['+', '*', '/', '-']
    for i in exp:
        if i in "0123456789":
            push(i,stack)
        elif i in operators:
            number2 = stack.pop()
            number1 = stack.pop()
            operator = i
            result = eval_post(number2, number1 ,operator,stack)
            push(result,stack)
            print result


if __name__ == '__main__':
    main()
            



