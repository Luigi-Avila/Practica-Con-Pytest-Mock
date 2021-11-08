from unittest import mock
import pytest
from monitor import main

#Prueba de integracion para la funcion de calculation_suma
#Particion de equivalencia
# numeros de entrada y salida positivos, negativos y ceros
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

#Prueba de integracion para la funcion de calculation_resta
#Particion de equivalencia
#Numeros de entrada y salida positivos, negativos y ceros
numerosArrayRestaExpected = [
    (1, -1, 2),
    (-1, 0, -1),
    (0, 0, 0),
]
@pytest.mark.parametrize("numberA, numberB, expected", numerosArrayRestaExpected)
def test_calculation_resta(numberA, numberB, expected):
    expected_result = expected
    process = main.calculation_resta(numberA, numberB)
    assert process == expected_result

#Prueba de integracion para la funcion de calculation_multiplication
#Particion de equivalencia
#Numeros de entrada y salida positivos, negativos y ceros
numerosArrayMultiExpected = [
    (1, -1, -1),
    (-2, 0, 0),
    (0, 1, 0),
    (1, 1, 1),
    (0.9, -1, -0.9)
]
@pytest.mark.parametrize("numberA, numberB, expected", numerosArrayMultiExpected)
def test_calculation_multiplicacion(numberA, numberB, expected):
    expected_result = expected
    process = main.calculation_multiplicacion(numberA, numberB)
    assert process == expected_result

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
    