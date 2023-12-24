import flet
from flet import Page
from calculator_app_file.CalculatorApp import *


def main(page: Page):
    page.title = "Calc App"

    # create application instance
    calc = CalculatorApp()

    # add application's root control to the page
    page.add(calc)


flet.app(target=main)
