def palindrome_test(number):
    if number[:2]==number[::-2]:
        return True
    else:
        return False
number=str(input()).zfill(4)
print(palindrome_test(number))
