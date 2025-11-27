from is_even import *

def test_even1():
    assert is_even(10) is True

def test_even2():
    assert is_even(101) is False

def test_even3():
    assert is_even(0) is True

def test_even4():
    assert is_even(-3) is False

def test_for_forbidden_operators():
    with open('is_even.py') as f:
        p = f.read()
        if '*' in p:
            raise ValueError("Use of * not permitted")
    
        if '%' in p:
            raise ValueError("Use of % not permitted")
    
        if '/' in p:
            raise ValueError("Use of / not permitted")

        

