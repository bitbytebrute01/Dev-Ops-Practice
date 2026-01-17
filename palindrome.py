def palindrome(text):
    rev = text[::-1]
    if text == rev:
        return "Palindrome"
    else:
        return "Not Palindrome"