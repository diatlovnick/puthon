def is_int(task: str):    
      while True:      
            try:
                  input_number = int(input(task))
                  return input_number
                  True
            except ValueError:
                  print('вы ввели не число')

      