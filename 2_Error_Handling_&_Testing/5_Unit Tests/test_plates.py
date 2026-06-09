from plates import is_valid

def test_Length():
    assert is_valid("AD1234") == True
    assert is_valid("AD") == True
    assert is_valid("A") == False
    assert is_valid("AD12345") == False

def test_FristTwo():
    assert is_valid("1234AD") == False
    assert is_valid("A1D234") == False
    assert is_valid("DA12") == True
    assert is_valid("ABCDE") == True

def test_Digits():
    assert is_valid("AD0123") == False
    assert is_valid("AD123C") == False
    assert is_valid("ADC210") == True
    assert is_valid("123456") == False

def test_Punctuations():
    assert is_valid("AD!$34") == False
    assert is_valid("ADCB@#") == False
    assert is_valid("AB;'.]") == False


