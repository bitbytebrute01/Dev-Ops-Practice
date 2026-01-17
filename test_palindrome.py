from palindrome import palindrome

def test01():
    assert palindrome("madam") == "Palindrome"

def test02():
    assert palindrome("gadag") == "Palindrome"

def test03():
    assert palindrome("hubli") == "Not Palindrome"
