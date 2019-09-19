def rle(str_test):
    if set(str_test).difference({'Q','W','E','R','T','Y','U','I','O','P','A','S','D','F','G','H','J','K','L','Z','X','C','V','B','N','M'})=={}:
        answ="error"
    elif str_test="":
        answ=""
    else:
        first_letter = str_test[0]
        j = 1
        words = []
        for i in range(1, len(str_test)):
            if str_test[i] == first_letter:
                j = j + 1
            else:
                words.append(first_letter)
                if j != 1:
                    words.append(j)
                first_letter = str_test[i]
                j = 1
        words.append(first_letter)
        if j != 1:
            words.append(j)
        answ=''.join(map(str, words))
    return answ


str_test="ABCDEFGHH"
print(rle(str_test))

