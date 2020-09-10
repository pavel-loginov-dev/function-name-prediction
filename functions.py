import json


def append_functions_infile(file_name, functions):
    '''Функция принимает на вход назване json файла и последовательность
    функций, и добавляет функции в конец файла'''
    with open(file_name, 'a') as json_file:
        for function in functions:
            json.dump(function, json_file)
            json_file.write('\n')

def get_funcs(module):
    '''В функцию подается модуль (последовательность узлов программы).
    Функция выбирает слайсы относящиеся к функциям и возвращает слайсы
    этих функций.
    
    module[i] -> node
    node -> {'type':str, 'children':list, 'value':str}
    node['children'][i] -> int
    '''
    functions = []
    i = 0
    while i < len(module):
        if module[i]['type'] == 'FunctionDef':
            last_child = module[i]['children'][-1]
            functions.append(module[i:last_child])
            i = last_child+1
        else:
            i+=1
    return functions

def load_portion_functions(file_name, pos, lines):
    '''Функция загружает функции из датасета, читая датасет с
    определенной позиции (pos) и определенное количество строк
    (lines).
    Returns:
        * functions [list]
        * last_position [int]
    '''
    functions = []
    with open(file_name, 'r') as json_file:
        json_file.seek(pos)
        i = lines
        while i != 0:
            functions.extend(get_funcs(json.loads(json_file.readline())))
            i-=1
        return functions, json_file.tell()


