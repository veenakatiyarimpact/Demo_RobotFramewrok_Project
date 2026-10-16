def printDetails(**kwargs):
    for key,value in kwargs.items():
        print(f'{key} : {value}')

printDetails(name="Veena",Add="Pune",age=30,Sex="F");