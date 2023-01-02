import View
import Model

def input_first(): # действия ниже объедили в функцию
    number = View.input_number() #взяли значение из View
    Model.set_first(number) #передали в Model

def input_second(): # действия ниже объедили в функцию
    while True:
        number = View.input_number() #взяли значение из View
        if Model.get_operation() == '/' and number == 0:
            View.print_division_to_zero()
        else:
            Model.set_second(number) #передали в Model
            break
def input_operation():
    oper = View.input_operation()
    Model.set_operation(oper)

def solution():
    oper = Model.get_operation()
    if oper == '+':
        Model.addition()
    elif oper == '-':
        Model.difference()
    elif oper == '*':
        Model.multiplication()
    elif oper == '/':
        Model.division()
    #else:
    #elif oper == '=':
     #   return True

    #result = Model.get_result()
    result_string = f'{Model.get_first()}{Model.get_operation()}{Model.get_second()} = {Model.get_result()}'
    View.print_to_console(result_string)
    Model.set_first(Model.get_result())
    #return False
def start():
    input_first()
    while True:
        input_operation()
        if Model.get_operation() == '=':
            View.log_off()
            break
        input_second()
        solution()

