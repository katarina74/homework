def dist(n):
    L=[1/i for i in range(1,n+1)]
    return ' '.join(["полное расстояние: ",str(sum(L)),", расстоние до работы: ",str(sum([((-1)**i)*L[i] for i in range(n)]))])

