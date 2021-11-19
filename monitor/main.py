def calculation_suma(a, b):
    return a + b

def calculation_resta(a,b):
    return a - b

def calculation_multiplicacion(a,b):
    mult = a * b
    mult = round(mult, 2)
    return mult

def valida(a,b):
    process_Sum = calculation_suma(a,b)
    process_Mul = calculation_multiplicacion(a,b)
    
    if isinstance(process_Sum, (int, float, complex)) and isinstance(process_Mul, (int, float, complex)):
        return 'success'
    else:
        return 'Fail'

def positive_negative(a, b):
    process_Sum = calculation_suma(a,b)
    # process_Mul = calculation_multiplicacion(a,b)
    if process_Sum > 0:
        return 'positive'
    elif process_Sum < 0:
        return 'negative'
    else:
        return 'neutro'


def make_a_dict_suma(a, b):
    operation = calculation_suma(a,b)
    return {"a": a, "b": b, "result": operation}

res = valida(5,6)
print(res)
resul = calculation_multiplicacion(0.1, 0.2)
print(resul)