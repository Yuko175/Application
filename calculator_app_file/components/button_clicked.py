def button_clicked(self, e):
    data = e.control.data
    if self.result.value == "Error" or data == "AC":
        self.result.value = "0"
        self.reset()

    elif data in ("1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "."):
        if self.result.value == "0" or self.new_operand == True:
            self.result.value = data
            self.new_operand = False
        else:
            self.result.value = self.result.value + data

    elif data in ("+", "-", "*", "/"):
        self.result.value = self.calculate(
            self.operand1, float(self.result.value), self.operator
        )
        self.operator = data
        if self.result.value == "Error":
            self.operand1 = "0"
        else:
            self.operand1 = float(self.result.value)
        self.new_operand = True

    elif data in ("="):
        self.result.value = self.calculate(
            self.operand1, float(self.result.value), self.operator
        )
        self.reset()

    elif data in ("%"):
        self.result.value = float(self.result.value) / 100
        self.reset()

    elif data in ("+/-"):
        if float(self.result.value) > 0:
            self.result.value = "-" + str(self.result.value)

        elif float(self.result.value) < 0:
            self.result.value = str(self.format_number(abs(float(self.result.value))))

    self.update()
