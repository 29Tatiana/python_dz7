def add_to_log(data):
    with open('log.csv', 'a') as file:
        file.write(f'{data};\n')