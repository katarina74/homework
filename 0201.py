def findErrors(str1):
    numberOfErrors=0
    for i in range(len(str1)-1):
        if str1[i:i+2] in {"жы", "шы", "чя", "щя"}:
            numberOfErrors=numberOfErrors+1
    return numberOfErrors

print("число ошибок: ", findErrors(input()))
