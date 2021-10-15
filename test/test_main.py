from unittest import mock
import pytest
from monitor import main

#Prueba unitaria para la funcion de suma, mandar un valor y comparar con un resultado esperado
def test_calculation_suma():
    expected_result = 9
    process = main.calculation_suma(4, 5)
    assert process == expected_result

#Prueba unitaria para la funcion de multiplicacion, mandar un valor y comparar con un resultado esperado
def test_calculation_multiplicacion():
    expected_result = 20
    process = main.calculation_multiplicacion(4,5)
    assert process == expected_result

#Prueba unitaria para la funcion de suma, con el decorador de pytest parametrize, manda los 2 valores a trabajar y el 3 valor es el esperado
@pytest.mark.parametrize("a, b, expected_result", [
    (1, 2, 3),
    (5, 5, 10),
    (3, 2, 5),
    (8, 2, 10),
    (4, 4, 8)
])
def test_calculation_suma_param(a, b, expected_result):
    process = main.calculation_suma(a,b)
    assert process == expected_result

#Prueba unitaria para la funcion de multiplicacion, con el decorador parametrize
#Se ingresaron valores negativos para validar que se pueden recibir valores de todo tipo
#Se ingresaron algunos valores invertidos para validar que hace la funcion de multiplicar
@pytest.mark.parametrize("a, b, expected_result", [
    (4, 3, 12),
    (3, 2, 6),
    (-5, 3, -15),
    (2, 3, 6),
    (0, 0, 0)
])
def test_calculation_multiplicacion_param(a, b, expected_result):
    process = main.calculation_multiplicacion(a, b)
    assert process == expected_result

#Prueba de integracion para la funcion de valida
#mockeando 2 funciones
#Usando el decorador Mock para no testear Suma y multiplicacion
@mock.patch('monitor.main.calculation_suma', return_value=5)
@mock.patch('monitor.main.calculation_multiplicacion', return_value=6)
def test_valida_mock(sum, multi):
    process = main.valida(3, 2)
    expected_result = 'success'
    assert process == expected_result


#Prueba de integracion para la funcion de diccionario
#mockeando solo una funcion
@mock.patch('monitor.main.calculation_suma', return_value = 5)
def test_make_a_dick_suma(sum):
    my_dict = main.make_a_dict_suma(4,1)
    expected_dict = {"a": 4, "b": 1, "result": 5}
    assert my_dict == expected_dict

#Prueba de integracion para la funcion de diccionario
#combinando mock y parametrize para probar varias posibilidades en el codigo como numeros negativos
#parametrize estatico
@pytest.mark.parametrize("a, b, expected_result",[
    (4, 2, 6),
    (5, 6, 11),
    (5, 2, 7),
    (-5, 5, 0),
    (-3, 7, 4)])

def test_make_a_dick_suma_param(a, b, expected_result):
    with mock.patch('monitor.main.calculation_suma', return_value= expected_result):
        my_dict = main.make_a_dict_suma(a,b)
    expected_dict = {"a": a, "b": b, "result": expected_result}
    assert my_dict == expected_dict


# Prueba unitaria para la funcion de suma
# Enviando un array al parametrize para que sea dinamico
# Por motivos de aprendizaje se coloco el arreglo arriba de la funcion, es una buena paractica ponerlo abajo de los imports al principio del codigo
numerosArray = [
    (1, 3, 4),
    (2, 9, 11),
    (5, 4, 9),
    (-5, 4, -1),
    (0, 0, 0)
]
@pytest.mark.parametrize("numberA, numberB, expected", numerosArray)
def test_calculation_suma_param_array(numberA, numberB, expected):
    process = main.calculation_suma(numberA, numberB)
    expected_result = expected
    assert process == expected_result

# Prueba de integracion para la funcion de valida
# Enviando 2 arrays al parametrize para que sea dinamico
# Combinando 2mock y parametrize
# En este caso un test fallo, al probar 0, 0, 0, la validacion de la funcion valida tomaba 0 como un valor que no existia y daba un resultado diferente al esperado
# Se agrego a la linea de codigo 14 or process_Sum == 0 and process_Mul == 0: y ahora sale correcto el test
@pytest.mark.parametrize("numberA, numberB, expected", numerosArray)
def test_valida(numberA, numberB, expected):
    with mock.patch('monitor.main.calculation_suma', return_value= expected):
        with mock.patch('monitor.main.calculation_multiplicacion', return_value= expected):
            process = main.valida(numberA, numberB)
    expected_result = 'success'
    assert process == expected_result
