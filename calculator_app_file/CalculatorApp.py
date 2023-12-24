import flet
from flet import UserControl
from calculator_app_file.components.build import build as components_build
from calculator_app_file.components.button_clicked import (
    button_clicked as components_button_clicked,
)
from calculator_app_file.components.format_number import (
    format_number as components_format_number,
)
from calculator_app_file.components.calculate import calculate as components_calculate
from calculator_app_file.components.reset import reset as components_reset


class CalculatorApp(UserControl):
    def build(self):
        return components_build(self)

    def button_clicked(self, e):
        components_button_clicked(self, e)

    def format_number(self, num):
        return components_format_number(num)

    def calculate(self, operand1, operand2, operator):
        return components_calculate(self, operand1, operand2, operator)

    def reset(self):
        components_reset(self)
