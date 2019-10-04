def deledeDuplicates(L):
    new_L=[]
    for el in L:
        if not(el in new_L):
            new_L.append(el)
    return new_L

    
