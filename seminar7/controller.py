import model
import view

def button_click():
    value_a = view.input_complex()
    value_b = view.input_complex()
    model.init(value_a,value_b)
    res = model.sum
    view.view_data(res)