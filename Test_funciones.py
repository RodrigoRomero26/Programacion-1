import pytest
from funciones import *
@pytest.mark.parametrize("dni, expected",[
    ("44310653", True),
])
def test_dnivalidator(dni, expected):
    assert dnivalidator(dni) == expected

@pytest.mark.parametrize("phrase, longi",[
    ("juan carlos", 6),
])
def test_lastwordlen(phrase, longi):
    assert lastwordlen(phrase) == longi

@pytest.mark.parametrize("word, long",[
    ("hola", "4"),
])
def test_wordlen(word, long):
    assert wordlen(word) == long

@pytest.mark.parametrize("phrase, pos, resul",[
    ("hola como estas",1,"como"),
])
def test_wordselector(phrase,pos,resul):
    assert wordselector(phrase,pos) == resul

@pytest.mark.parametrize("num1, num2, resul",[
    (10,5,True),
])
def test_ismult(num1,num2,resul):
    assert ismult(num1,num2) == resul

@pytest.mark.parametrize("temp1, temp2, resul",[
    (15,20,17.5),
])
def test_medtemp(temp1,temp2,resul):
    assert medtemp(temp1,temp2) == resul

@pytest.mark.parametrize("phrase,resul",[
    ("hola como estas","h o l a  c o m o  e s t a s "),
])
def test_letterbyletter(phrase, resul):
    assert letterbyletter(phrase) == resul

@pytest.mark.parametrize("numlist, result",[
    ([1,2,3,4,5],[1,5]),
])
def test_minmaxlist(numlist, result):
    assert minmaxlist(numlist) == result

@pytest.mark.parametrize("num, result",[
    (5,10),
])
def test_double(num, result):
    assert double(num) == result

@pytest.mark.parametrize("phrase, result",[
    ("hola como estas", {"hola":4,"como":4,"estas":5})
])
def test_phraselen(phrase, result):
    assert phraselen(phrase) == result

@pytest.mark.parametrize("x,y, result",[
    (5,5,50),
])
def test_modcalc(x,y,result):
    assert modcalc(x,y) == result

@pytest.mark.parametrize("num, result",[
    (7, True),
])
def test_isprime(num, result):
    assert is_prime(num) == result

@pytest.mark.parametrize("num, result",[
    (5,120),
])
def test_factorial(num, result):
    assert factorial(num) == result

@pytest.mark.parametrize("num, digit, result",[
    (123455,5,2),
])
def test_digitcount(num, digit, result):
    assert digitcount(num, digit) == result