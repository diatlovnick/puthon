import interface
#import change as c
import work_with_information as w
import view as v
import delete as d
def run():
    run = True
    while run:
        option = interface.start()
        if option == '5':
            return
        elif option == '1':
            v.view_list()
        elif option == '2':
            w.enter_task()
#        elif option == '3':
#            c.search_change()
        elif option == '4':
            d.delete_task()
run()