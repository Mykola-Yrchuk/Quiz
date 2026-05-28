from Quiz import is_correct

def test_correct_answer():
    assert is_correct("8", "8") == True

def test_wrong_answer():
    assert is_correct("7", "8") == False
