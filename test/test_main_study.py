from unittest import mock
from py import process
import pytest
from monitor import main

#Prueba unitaria para la funcion de calculation_suma
#Particion de equivalencia
# numeros de entrada y salida positivos, negativos ceros y decimales
numerosArraySumaExpected = [
    (2, -1, 1),
    (-1, 0, -1),
    (0, 0, 0),
    (1, -0.9, 0.1),
    (-0.8, -0.1, -0.9)
]
@pytest.mark.parametrize("numberA, numberB, expected", numerosArraySumaExpected)
def test_calculation_suma(numberA, numberB, expected):
    expected_result =  expected
    process = main.calculation_suma(numberA, numberB)
    assert process == expected_result

#Prueba unitaria para la funcion de calculation_resta
#Particion de equivalencia
#Numeros de entrada y salida positivos, negativos, ceros y decimales
numerosArrayRestaExpected = [
    (1, -1, 2),
    (-1, 0, -1),
    (0, 0, 0),
    (0.8, -0.1, 0.9),
    (-0.8, 0.1, -0.9)
]
@pytest.mark.parametrize("numberA, numberB, expected", numerosArrayRestaExpected)
def test_calculation_resta(numberA, numberB, expected):
    expected_result = expected
    process = main.calculation_resta(numberA, numberB)
    assert process == expected_result

#Prueba unitaria para la funcion de calculation_multiplication
#Particion de equivalencia
#Numeros de entrada y salida positivos, negativos, ceros y decimales
numerosArrayMultiExpected = [
    (1, -1, -1),
    (-2, 0, 0),
    (1, 1, 1),
    (0.9, -0.1, -0.09)
]
@pytest.mark.parametrize("numberA, numberB, expected", numerosArrayMultiExpected)
def test_calculation_multiplicacion(numberA, numberB, expected):
    expected_result = expected
    process = main.calculation_multiplicacion(numberA, numberB)
    assert process == expected_result

# Pruebas de integracion para la funcion de valida

numerosArrayValidaExpected = [
    (1, 1, 1, 'success'),
    (' ', ' ', ' ', 'Fail'),
    (0, 0, 0, 'success')
]
@pytest.mark.parametrize("numberA, numberB, value, expected", numerosArrayValidaExpected)
def test_valida(numberA, numberB, value, expected):
    with mock.patch('monitor.main.calculation_suma', return_value = value):
        with mock.patch('monitor.main.calculation_multiplicacion', return_value = value):
            process = main.valida(numberA, numberB)
    expected_result = expected
    assert process == expected_result

# Prueba de integracion para la funcion positive_negative
# Particion de equivalencia y analisis de valores limite
numerosArraySumPos_negativeExpected = [
    (0, 0.1, 0.1, 'positive'),
    (0, 0, 0, 'neutro'),
    (-0.1, 0, -0.1, 'negative')
]
@pytest.mark.parametrize("numberA, numberB, value, expected", numerosArraySumPos_negativeExpected)
def test_positive_negative(numberA, numberB, value, expected):
    with mock.patch('monitor.main.calculation_suma', return_value = value):
        process = main.positive_negative(numberA, numberB)
    expected_result = expected
    assert process == expected_result


# MIS PRACTICAS
# #Prueba de integracion para la funcion de valida
# # Enfoque al resultado
# numerosArrayValidaExpected = [
#     (1, -0.1, 'success'),
#     (0, 0.1, 'success'),
#     (0, 0, 'success'),
#     ( 'b', 'a', 'Fail')
# ]

# @pytest.mark.parametrize("numberA, numberB, expected", numerosArrayValidaExpected)
# def test_valida(numberA, numberB, expected):
#     expected_result = expected
#     process_Suma = main.valida(numberA, numberB)
#     assert process_Suma == expected_result

#Prueba de integracion para la funcion de positive_negative
#mock y parametrize
#Analisis de valores limites y particion de equivalencia
#Probar valores de -1, 0 y 1 
# numerosArraySuma = [
#     (-1, 1, 0),
#     (0, 1, 1),
#     (-2, 1, -1)
# ]

# numerosArraySumaExpected = [
#     ('neutro'),
#     ('positive'),
#     ('negative')
# ]

# @pytest.mark.parametrize("expectedStr", numerosArraySumaExpected)
# @pytest.mark.parametrize("numberA, numberB, expected", numerosArraySuma)
# def test_positive_negative(numberA, numberB, expected, expectedStr):
#     with mock.patch('monitor.main.calculation_suma', return_value = expected):
#         process = main.positive_negative(numberA, numberB)
#         expected_result = expectedStr
#     assert process == expected_result

