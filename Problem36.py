def palindrome(number):
    if number[0] == number[5]:
        if number[1] == number[4]:
            if number[2] == number[3]:
                return True
    else:
        return False

    