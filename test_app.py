from app import soma

def test_soma_positiva():
    assert soma(2, 3) == 5

def test_soma_negativa():
    assert soma(-1, 1) == 0

def test_soma_com_erro():
    assert soma(2, 2) == 3