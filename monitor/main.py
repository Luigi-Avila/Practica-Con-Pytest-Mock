def calculation_suma(a, b):
    return a + b

def calculation_resta(a,b):
    return a - b

def calculation_multiplicacion(a,b):
    return a * b

def valida(a,b):
    process_Sum = calculation_suma(a,b)
    process_Mul = calculation_multiplicacion(a,b)
    print('esto retorna de suma --> ', process_Sum, "esto retorna de multi --> ", process_Mul)
    if process_Sum and process_Mul or process_Sum == 0 and process_Mul == 0:
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

