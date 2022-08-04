import model
import view

def button_click():
    value_a = view.input_complex()
    value_b = view.input_complex()
    value_a, value_b = model.init(value_a, value_b)
    znac = view.input_znac()
    if znac =="+":
        res = model.sum(value_a, value_b)
    elif znac == "-":
        res = model.sub(value_a, value_b)
    elif znac == "*":
        res = model.mult(value_a, value_b)
    elif znac == "/":
        res = model.div(value_a, value_b)
    else:
        print('ввели неправильное ')

    
    view.view_data(res)
button_click()