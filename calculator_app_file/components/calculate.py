def calculate(self, operand1, operand2, operator):
    if operator == "+":
        return self.format_number(operand1 + operand2)

    elif operator == "-":
        return self.format_number(operand1 - operand2)

    elif operator == "*":
        return self.format_number(operand1 * operand2)

    elif operator == "/":
        if operand2 == 0:
            return "Error"
        else:
            return self.format_number(operand1 / operand2)
