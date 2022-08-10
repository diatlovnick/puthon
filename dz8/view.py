from importlib.resources import path
import json

path  = r'C:\Users\w01NB001\Documents\GeekBrains\python\dz8\todolist.json'
def view_list():
     with open(path, 'r', encoding='UTF-8') as file:
         data = json.load(file)
         for i in range(0,len(data)):
             print(data[i])
#view_list()