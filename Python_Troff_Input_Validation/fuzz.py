from conftest import testin

def test_dot():
    assert testin != ".\n"

def test_no_backslash():
    for i in range(len(testin) - 1):
        assert not (testin[i:i+2] == "\\D" and not (32 <= ord(testin[i+2]) <= 126))
        
def test_8bit():
    for i in range(len(testin) - 1):
        assert ord(testin[i]) <= 127 or testin[i + 1] != '\n'
        
