import Model7
import View7
import Logger7

def input_equation():
    equ_str = View7.input_equation()
    Model7.set_equation(equ_str)


def start():
    input_equation()
    Model7.solution_equation()
    View7.print_to_console(f'{Model7.get_equation()} = {Model7.get_result()}')
    Logger7.add_log(f'{Model7.get_equation()} = {Model7.get_result()}')