def plus(m1,m2):
    lm1=len(m1)
    lm2=len(m2)

    result=[]
    k=0

    for i in range(1,min(lm1,lm2)+1):
        j=m1[-i]+m2[-i]+k
        k=j//10
        result.insert(0,j%10)
    
    if lm1>lm2:
        result.insert(0,m1[-(lm2+1)]+k)
        result=m1[0:lm1-lm2-1]+result
    elif lm1<lm2:
        result.insert(0,m2[-(lm1+1)]+k)
        result=m2[0:lm2-lm1-1]+result
    elif k!=0:
        result.insert(0,k)
    while True:
        if result[0]==0 and len(result)>1:
            del result[0]
        else:
            break
    return result

def minus(m1,m2):
    lm1=len(m1)
    lm2=len(m2)

    if lm1>lm2:
        negative_number=False
    elif lm1==lm2:
        negative_number=True
        for i in range(lm1):
            if m1[i]>m2[i]:
                negative_number=False
                break
    else:
        negative_number=True

        m1,m2=m2,m1
        lm1,lm2=lm2,lm1
    
    result=[]
    k=0

    for i in range(1,min(lm1,lm2)+1):
        j1=m1[-i]
        j2=m2[-i]
        if j1>j2:
            result.insert(0,j1-j2-k)
            k=0
        elif j1==j2 and k==0:
            result.insert(0,j1-j2)
        else:
            result.insert(0,10+j1-j2-k)
            k=1
        
    while True:
        if result[0]==0 and len(result)>1:
            del result[0]
        else:
            break
    
    if k==0:
        result=m1[0:lm1-lm2]+result
    else:
        for i in range(lm1-lm2-1,-1,-1):
            if m1[i]>0:
                result.insert(0,m1[i]-k)
                result=m1[0:lm1-lm2-1]+result
                break
            else:
                result.insert(0,m1[i]-k)

    if negative_number:
        result=[-el for el in result]
    
    return result

# если число отрицательно, то каждый элемент массива отрицательный
m1=[int(el) for el in input().split()]
z=input("+ or -")
m2=[int(el) for el in input().split()]

if z=="+":
    if m1[1]>0 and m2[0]>0:
        print(plus(m1,m2))
    elif m1[0]>0 and m2[0]<0:
        print(minus(m1,m2))
    elif m1[0]<0 and m2[0]<0:
        print([- el for el in
               plus(
            [-el for el in m1],
            [-el for el in m2])])
    else:
        print(minus(m2,[-el for el in m1]))
else:
    if m1[1]>0 and m2[0]>0:
        print(minus(m1,m2))
    elif m1[0]>0 and m2[0]<0:
        print(plus(m1,m2))
    elif m1[0]<0 and m2[0]<0:
        print(minus(
            [-el for el in m1],
            [-el for el in m2]))
    else:
        print([-el for el in plus(m1,m2)])
